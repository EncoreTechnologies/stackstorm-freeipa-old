import re
import requests
import six
import urllib3
from ipa_command_args_options import IPA_COMMAND_ARGS_OPTIONS

from st2common.runners.base_action import Action

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()  # pylint: disable=no-member


CONNECTION_OPTIONS = [
    'server',
    'username',
    'password',
    'verify_ssl',
]


class IpaAction(Action):

    def __init__(self, config):
        super(IpaAction, self).__init__(config)
        self.session = requests.Session()

    def _resolve_connection(self, **kwargs):
        """ Lookup connection, by name, specified by the 'connection' parameter
        during action invocation from the connection dict stored in the config
        """
        # if there are no connection specified in the config, we have nothing to lookup
        if not self.config.get('connections'):
            return kwargs

        # get the name of connection asked for during action invocation
        con_name = kwargs.get('connections')
        if not con_name:
            return kwargs

        # if we couldn't find the connection in the config (by name),
        # then try checking if a 'default' connection is specified
        # otherwise raise an error
        if con_name not in self.config['connections']:
            con_name = 'default'
            if con_name not in self.config['connections']:
                raise ValueError('Unable to find connection named "{}" or "default" in config'
                                 .format(con_name))

        # lookup the credential by name
        connection = self.config['connections'][con_name]
        for k, v in six.iteritems(connection):
            # skip if the user explicitly set this property during action invocation
            if kwargs.get(k) is not None:
                continue

            # only set the property if the value in the credential object is set
            if v is not None:
                kwargs[k] = v

        return kwargs

    def _validate_connection(self, connection):
        """Ensures that all required parameters are in the connection. If a
        required parameter is missing a KeyError exception is raised.
        :param connection: connection to validate
        :returns: True if the connection is valid
        """
        for key in CONNECTION_OPTIONS:
            # ensure the key is present in the connection?
            if connection.get(key, None) is not None:
                continue

            if 'connection' in connection:
                raise KeyError("/opt/stackstorm/configs/freeipa.yaml missing key connections.{}.1}"
                               .format(connection['connection'], key))
            else:
                raise KeyError("Because the 'connection' action parameter was"
                               " not specified, the following action parameter"
                               " is required: {0}".format(key))
        return True

    def _raise_for_status(self, response):
        """Raises stored :class:`requests.HTTPError`, if one occurred.
        Copied from requests package, but adds in response.content to the exception
        message.
        """
        http_error_msg = ''
        if isinstance(response.reason, bytes):
            # We attempt to decode utf-8 first because some servers
            # choose to localize their reason strings. If the string
            # isn't utf-8, we fall back to iso-8859-1 for all other
            # encodings. (See PR #3538)
            try:
                reason = response.reason.decode('utf-8')
            except UnicodeDecodeError:
                reason = response.reason.decode('iso-8859-1')
        else:
            reason = response.reason

        error_side = ''
        if 400 <= response.status_code < 500:
            error_side = 'Client'
        elif 500 <= response.status_code < 600:
            error_side = 'Server'

        if error_side:
            http_error_msg = "{0} {1} Error: {2} for url: {3}\n{4}".format(response.status_code,
                                                                           error_side,
                                                                           reason,
                                                                           response.url,
                                                                           response.content)
            raise requests.HTTPError(http_error_msg, response=response)

    def _ipa_url(self, server, endpoint=None):
        if not endpoint:
            endpoint = ''
        return 'https://{0}/ipa{1}'.format(server, endpoint)

    def _login(self, connection):
        """Attempts to login to the FreeIPA server given the connection information.
        :param connect: dict containing values for 'server', 'username' and 'password'
        :returns: login session token upon successful login
        :rtype: string
        """
        server = connection['server']
        username = connection['username']
        password = connection['password']

        url = self._ipa_url(server, '/session/login_password')
        headers = {
            "referer": self._ipa_url(server),
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }
        payload = "user={0}&password={1}".format(username, password)

        response = self.session.post(url,
                                     headers=headers,
                                     data=payload)
        self._raise_for_status(response)

        session = ''
        if 'ipa_session' in response.cookies:
            session = response.cookies['ipa_session']
        else:
            raise RuntimeError('IPA server did not return a cookie named "ipa_session"')

        self.logger.debug('Successfully logged in as {0}'.format(username))
        return session

    def _execute(self, session, server, api_version=None, **kwargs):
        """Called by main entry point for the StackStorm actions to execute the operation.
        :returns: json-encoded content of the response to the HTTP request, if any
        """
        method = kwargs['method']
        # args go into an array
        args = []
        # options go into a hash where it's the option name : value
        options = {}
        # lookup which kwargs are args vs options based on the auto-generated
        # data, this comes from etc/generate_actions.py
        method_args_options = IPA_COMMAND_ARGS_OPTIONS[method]
        for arg in method_args_options['args']:
            if arg in kwargs:
                args.append(kwargs[arg])
        for option in method_args_options['options']:
            if option in kwargs:
                options[option] = kwargs[option]

        if api_version:
            options['version'] = api_version

        url = self._ipa_url(server, '/session/json')
        headers = {
            "referer": self._ipa_url(server),
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "id": 0,
            "method": method,
            "params": [
                args,
                options
            ]
        }

        response = self.session.post(url,
                                     headers=headers,
                                     json=payload,
                                     cookies={'ipa_session': session})
        self._raise_for_status(response)

        result_data = response.json()
        if 'error' in result_data and result_data['error']:
            return (False, result_data)
        return (True, result_data)

    def _get_api_version(self, session, server):
        # get the server version
        response = self._execute(session, server, method='ping')
        ping_good = response[0]
        data = response[1]

        # retrieve server version from result and add it to the
        # options for the real request.
        # this avoids the error message:
        # "API Version number was not sent, forward compatibility not
        # guaranteed. Assuming server's API version, x.xxx"
        api_version = None
        if ((ping_good and
             ('result' in data) and
             ('summary' in data['result']))):
            # parse the API version from a "summary" string that looks like:
            # "IPA server version 4.5.0. API version 2.228"
            match = re.search('API version ([0-9]+\.[0-9]+)',
                              data['result']['summary'])
            if match:
                api_version = match.group(1)

        self.logger.debug('API Version: {0}'.format(api_version))
        return api_version

    def run(self, **kwargs):
        connection = self._resolve_connection(**kwargs)
        self._validate_connection(connection)
        self.session.verify = connection['verify_ssl']

        if 'session' in kwargs and kwargs['session']:
            session = kwargs['session']
            server = kwargs['server']
        else:
            server = connection['server']
            session = self._login(connection)

        del kwargs['server']
        del kwargs['session']

        if kwargs['method'] == 'login':
            return session
        else:
            api_version = self._get_api_version(session, server)
            return self._execute(session, server, api_version=api_version, **kwargs)

import requests
import json

from st2actions.runners.pythonrunner import Action

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#                         (key, required, default)
CONFIG_CONNECTION_KEYS = [('server', True, ""),
                          ('username', True, ""),
                          ('password', True, "")]


class BaseAction(Action):

    def __init__(self, config):
        """Creates a new BaseAction given a StackStorm config object (kwargs works too)
        :param config: StackStorm configuration object for the pack
        :returns: a new BaseAction
        """
        super(BaseAction, self).__init__(config)
        self.session = requests.Session()

    def _get_del_arg(self, key, kwargs_dict):
        """Attempts to retrieve an argument from kwargs with key.
        If the key is found, then delete it from the dict.
        :param key: the key of the argument to retrieve from kwargs
        :returns: The value of key in kwargs, if it exists, otherwise None
        """
        if key in kwargs_dict:
            value = kwargs_dict[key]
            del kwargs_dict[key]
            return value
        else:
            return None

    def _resolve_connection(self, kwargs_dict):
        """Attempts to resolve the connection information by looking up information
        from action input parameters (highest priority) or from the config (fallback).
        :param kwargs_dict: dictionary of kwargs containing the action's input
        parameters
        :returns: a dictionary with the connection parameters (see: CONFIG_CONNECTION_KEYS)
        resolved.
        """
        connection_name = self._get_del_arg('connection', kwargs_dict)
        config_connection = None
        if connection_name:
            config_connection = self.config['freeipa'].get(connection_name)
            if not config_connection:
                raise KeyError("config.yaml missing connection: freeipa:{0}"
                               .format(connection_name))

        action_connection = {'connection': connection_name}

        # Override the keys in creds read in from the config given the
        # override parameters from the action itself
        # Example:
        #   'user' parameter on the action will override the username
        #   from the credential. This is useful for runnning the action
        #   standalone and/or from the commandline
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if key in kwargs_dict and kwargs_dict[key]:
                # use params from cmdline first (override)
                action_connection[key] = self._get_del_arg(key, kwargs_dict)
            elif config_connection and key in config_connection and config_connection[key]:
                # fallback to creds in config
                action_connection[key] = config_connection[key]
            else:
                if not required and default:
                    action_connection[key] = default

            # remove the key from kwargs if it's still in there
            if key in kwargs_dict:
                del kwargs_dict[key]

        return action_connection

    def _validate_connection(self, connection):
        """Ensures that all required parameters are in the connection. If a
        required parameter is missing a KeyError exception is raised.
        :param connection: connection to validate
        :returns: True if the connection is valid
        """
        for key, required, default in CONFIG_CONNECTION_KEYS:
            # ensure the key is present in the connection?
            if key in connection and connection[key]:
                continue

            # skip if this key is not required
            if not required:
                continue

            if 'connection' in connection:
                raise KeyError("config.yaml mising: freeipa:{0}:{1}"
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
        """Performs the login operation on the user
        :param connect: a dict containing values for 'server', 'username' and 'password'
        :returns: the session token upon successful login
        :rtype: string
        """
        server = connection['server']
        username = connection['username']
        password = connection['password']
        ipaurl = self._ipa_url(server, '/session/login_password')
        login_headers = {"referer": self._ipa_url(server),
                         "Content-Type": "application/x-www-form-urlencoded",
                         "Accept": "text/plain"}
        payload = "user={0}&password={1}".format(username, password)
        response = self.session.post(ipaurl,
                                     headers=login_headers,
                                     data=payload,
                                     verify=False)
        self._raise_for_status(response)

        session = ''
        if 'ipa_session' in response.cookies:
            session = response.cookies['ipa_session']
        else:
            raise RuntimeError('IPA server did not return a cookie named "ipa_session"')

        self.logger.debug('Successfully logged in as {0}'.format(username))
        return session

    def _execute(self, session, server, kwargs_dict):
        """Called by main entry point for the StackStorm actions to execute the operation.
        :returns: json-encoded content of the response to the HTTP request, if any
        """
        data = {"id": 0,
                "method": kwargs_dict['method'],
                "params": [kwargs_dict['args'],
                           kwargs_dict['options']]}
        url = self._ipa_url(server, '/session/json')
        headers = {"referer": self._ipa_url(server),
                   "Content-Type": "application/json",
                   "Accept": "application/json"}
        response = self.session.post(url,
                                     headers=headers,
                                     json=data,
                                     verify=False,
                                     cookies={'ipa_session': session})
        self._raise_for_status(response)
        result_data = response.json()
        if 'error' in result_data:
            return (False, result_data)
        return (True, results)

    def run(self, **kwargs):
        """Main entry point for the StackStorm actions to execute the operation.
        :returns: the result of the operation
        :return type: json-encoded content (same as make_req)
        """
        kwargs_dict = dict(kwargs)

        if 'session' in kwargs_dict and kwargs_dict['session']:
            session = kwargs_dict['session']
            server = kwargs_dict['server']
        else:
            connection = self._resolve_connection(kwargs_dict)
            self._validate_connection(connection)
            server = connection['server']
            session = self._login(connection)

        if kwargs_dict['method'] == 'login':
            return session
        else:
            return self._execute(session, server, kwargs_dict)

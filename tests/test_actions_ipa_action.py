from freeipa_base_action_test_case import FreeIPABaseActionTestCase
import ipa_action
from ipa_command_args_options import IPA_COMMAND_ARGS_OPTIONS

import copy
import mock
import requests


class TestActionsIpaAction(FreeIPABaseActionTestCase):
    __test__ = True
    action_cls = ipa_action.IpaAction

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, ipa_action.IpaAction)
        self.assertIsInstance(action.session, requests.Session)

    def test__resolve_connection_from_config(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection_config = self.config_good['connections'][connection_name]
        connection_expected = {'connection': connection_name}
        connection_expected.update(connection_config)
        connection_result = action._resolve_connection(connection=connection_name)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_from_config_missing(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'this_connection_doesnt_exist'
        with self.assertRaises(KeyError):
            action._resolve_connection(connection=connection_name)

    def test__resolve_connection_from_config_defaults(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection_config = self.config_good['connections'][connection_name]
        connection_expected = {'connection': connection_name}
        connection_expected.update(connection_config)
        connection_result = action._resolve_connection(connection=connection_name)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_from_kwargs(self):
        action = self.get_action_instance(self.config_blank)
        kwargs = {'connection': None,
                  'server': 'kwargs_server',
                  'username': 'kwargs_user',
                  'password': 'kwargs_password'}
        connection_expected = copy.deepcopy(kwargs)
        connection_result = action._resolve_connection(**kwargs)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_from_kwargs_defaults(self):
        action = self.get_action_instance(self.config_blank)
        kwargs = {'connection': None,
                  'server': 'kwargs_server',
                  'username': 'kwargs_user',
                  'password': 'kwargs_password'}
        connection_expected = copy.deepcopy(kwargs)
        connection_result = action._resolve_connection(**kwargs)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_from_kwargs_extras(self):
        action = self.get_action_instance(self.config_blank)
        kwargs = {'connection': None,
                  'server': 'kwargs_server',
                  'username': 'kwargs_user',
                  'password': 'kwargs_password',
                  "extra_key1": "extra_value1",
                  "extra_key2": 234}
        connection_expected = copy.deepcopy(kwargs)
        connection_result = action._resolve_connection(**kwargs)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_kwargs_overwrites_config(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'full'
        connection_config = self.config_good['connections'][connection_name]
        kwargs = {'connection': connection_name,
                  'server': 'kwargs_server',
                  'username': 'kwargs_user'}
        connection_expected = copy.deepcopy(kwargs)
        connection_expected['password'] = connection_config['password']
        connection_expected['verify_ssl'] = connection_config['verify_ssl']
        connection_result = action._resolve_connection(**kwargs)
        self.assertEqual(connection_result, connection_expected)

    def test__validate_connection(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        for key in ipa_action.CONNECTION_OPTIONS:
            connection[key] = "dummy value"
        result = action._validate_connection(connection)
        self.assertTrue(result)

    def test__validate_connection_missing_raises(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        with self.assertRaises(KeyError):
            action._validate_connection(connection)

    def test__validate_connection_none_raises(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        for key in ipa_action.CONNECTION_OPTIONS:
            connection[key] = None

        with self.assertRaises(KeyError):
            action._validate_connection(connection)

    def test__ipa_url(self):
        action = self.get_action_instance(self.config_blank)
        expected = "https://server.domain.tld/ipa/api/host_add"
        result = action._ipa_url("server.domain.tld", "/api/host_add")
        self.assertEqual(result, expected)

    def test__ipa_url_no_endpoint(self):
        action = self.get_action_instance(self.config_blank)
        expected = "https://server.domain.tld/ipa"
        result = action._ipa_url("server.domain.tld")
        self.assertEqual(result, expected)

    def test__login_success(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['connections']['base']

        expected_session = "session123"
        mock_response = mock.Mock(cookies={'ipa_session': expected_session},
                                  reason=None,
                                  status_code=200)
        mock_session = mock.Mock()
        mock_session.post.return_value = mock_response
        action.session = mock_session

        url = 'https://{0}/ipa/session/login_password'.format(connection['server'])
        headers = {"referer": 'https://{0}/ipa'.format(connection['server']),
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        payload = 'user={0}&password={1}'.format(connection['username'],
                                                 connection['password'])

        # execute
        result = action._login(connection)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             data=payload)
        self.assertEqual(result, expected_session)

    def test__login_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['connections']['base']

        mock_response = mock.Mock(cookies={'xxx': ''},
                                  reason=None,
                                  status_code=200)
        mock_session = mock.Mock()
        mock_session.post.return_value = mock_response
        action.session = mock_session

        url = 'https://{0}/ipa/session/login_password'.format(connection['server'])
        headers = {"referer": 'https://{0}/ipa'.format(connection['server']),
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        payload = 'user={0}&password={1}'.format(connection['username'],
                                                 connection['password'])

        # execute
        with self.assertRaises(RuntimeError):
            action._login(connection)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             data=payload)

    def test__login_http_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['connections']['base']

        mock_response = mock.Mock(cookies={'xxx': ''},
                                  reason=None,
                                  status_code=401)
        mock_session = mock.Mock()
        mock_session.post.return_value = mock_response
        action.session = mock_session

        url = 'https://{0}/ipa/session/login_password'.format(connection['server'])
        headers = {"referer": 'https://{0}/ipa'.format(connection['server']),
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        payload = 'user={0}&password={1}'.format(connection['username'],
                                                 connection['password'])

        # execute
        with self.assertRaises(requests.HTTPError):
            action._login(connection)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             data=payload)

    def test__create_payload(self):
        action = self.get_action_instance(self.config_good)

        method = 'hostgroup_show'
        args = IPA_COMMAND_ARGS_OPTIONS[method]['args']
        options = IPA_COMMAND_ARGS_OPTIONS[method]['options']
        kwargs = {
            'method': method,
        }
        expected_args = []
        for i, a in enumerate(args):
            kwargs[a] = i
            expected_args.append(i)

        expected_options = {}
        for i, o in enumerate(options):
            kwargs[o] = i
            expected_options[o] = i

        result = action._create_payload(**kwargs)
        self.assertEqual(result, {
            "id": 0,
            "method": method,
            "params": [
                expected_args,
                expected_options,
            ],
        })

    def test__create_payload_api_version(self):
        action = self.get_action_instance(self.config_good)

        method = 'hostgroup_show'
        args = IPA_COMMAND_ARGS_OPTIONS[method]['args']
        options = IPA_COMMAND_ARGS_OPTIONS[method]['options']
        kwargs = {
            'method': method,
        }
        expected_args = []
        for i, a in enumerate(args):
            kwargs[a] = i
            expected_args.append(i)

        expected_options = {}
        for i, o in enumerate(options):
            kwargs[o] = i
            expected_options[o] = i
        expected_options['version'] = 99

        result = action._create_payload(api_version=99, **kwargs)
        self.assertEqual(result, {
            "id": 0,
            "method": method,
            "params": [
                expected_args,
                expected_options,
            ],
        })

    def test__execute_success(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['connections']['base']

        server = connection['server']
        session = "session123"
        method = 'hostgroup_show'
        args = IPA_COMMAND_ARGS_OPTIONS[method]['args']
        options = IPA_COMMAND_ARGS_OPTIONS[method]['options']
        kwargs = {
            'method': method,
        }
        expected_args = []
        for i, a in enumerate(args):
            kwargs[a] = i
            expected_args.append(i)

        expected_options = {}
        for i, o in enumerate(options):
            kwargs[o] = i
            expected_options[o] = i

        expected_dict = {'result': 'value'}
        mock_response = mock.Mock(reason=None,
                                  status_code=200)
        mock_response.json.return_value = expected_dict

        mock_session = mock.Mock()
        mock_session.post.return_value = mock_response
        action.session = mock_session

        url = 'https://{0}/ipa/session/json'.format(server)
        headers = {"referer": 'https://{0}/ipa'.format(server),
                   "Content-Type": "application/json",
                   "Accept": "application/json"}
        payload = {"id": 0,
                   "method": kwargs['method'],
                   "params": [expected_args,
                              expected_options]}

        # execute
        result = action._execute(session, server, **kwargs)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             json=payload,
                                             cookies={'ipa_session': session})
        self.assertEqual(result, (True, expected_dict))

    def test__execute_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['connections']['base']

        server = connection['server']
        session = "session123"
        method = 'hostgroup_show'
        args = IPA_COMMAND_ARGS_OPTIONS[method]['args']
        options = IPA_COMMAND_ARGS_OPTIONS[method]['options']
        kwargs = {
            'method': method,
        }
        expected_args = []
        for i, a in enumerate(args):
            kwargs[a] = i
            expected_args.append(i)

        expected_options = {}
        for i, o in enumerate(options):
            kwargs[o] = i
            expected_options[o] = i

        expected_dict = {'error': 'value'}
        expected_result = (False, expected_dict)
        mock_response = mock.Mock(reason=None,
                                  status_code=200)
        mock_response.json.return_value = expected_dict

        mock_session = mock.Mock()
        mock_session.post.return_value = mock_response
        action.session = mock_session

        url = 'https://{0}/ipa/session/json'.format(server)
        headers = {"referer": 'https://{0}/ipa'.format(server),
                   "Content-Type": "application/json",
                   "Accept": "application/json"}
        payload = {"id": 0,
                   "method": kwargs['method'],
                   "params": [expected_args,
                              expected_options]}

        # execute
        result = action._execute(session, server, **kwargs)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             json=payload,
                                             cookies={'ipa_session': session})
        self.assertEqual(result, expected_result)

    def test__execute_http_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['connections']['base']

        server = connection['server']
        session = "session123"
        method = 'hostgroup_show'
        args = IPA_COMMAND_ARGS_OPTIONS[method]['args']
        options = IPA_COMMAND_ARGS_OPTIONS[method]['options']
        kwargs = {
            'method': method,
        }
        expected_args = []
        for i, a in enumerate(args):
            kwargs[a] = i
            expected_args.append(i)

        expected_options = {}
        for i, o in enumerate(options):
            kwargs[o] = i
            expected_options[o] = i

        mock_response = mock.Mock(reason=None,
                                  status_code=400)

        mock_session = mock.Mock()
        mock_session.post.return_value = mock_response
        action.session = mock_session

        url = 'https://{0}/ipa/session/json'.format(server)
        headers = {"referer": 'https://{0}/ipa'.format(server),
                   "Content-Type": "application/json",
                   "Accept": "application/json"}
        payload = {"id": 0,
                   "method": kwargs['method'],
                   "params": [expected_args,
                              expected_options]}

        # execute
        with self.assertRaises(requests.HTTPError):
            action._execute(session, server, **kwargs)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             json=payload,
                                             cookies={'ipa_session': session})

    @mock.patch('ipa_action.IpaAction._execute')
    def test__get_api_version(self, mock__execute):
        # setup
        action = self.get_action_instance(self.config_blank)

        ping_good = True
        data = {'result': {'summary': "API version 1.234"}}
        mock__execute.return_value = (ping_good, data)

        session = 'session123'
        server = 'server.domain.tld'

        # execute
        result = action._get_api_version(session, server)

        # verify
        self.assertEqual(result, "1.234")

    @mock.patch('ipa_action.IpaAction._execute')
    def test__get_api_version_missing(self, mock__execute):
        # setup
        action = self.get_action_instance(self.config_blank)

        ping_good = True
        data = {'result': {}}
        mock__execute.return_value = (ping_good, data)

        session = 'session123'
        server = 'server.domain.tld'

        # execute
        result = action._get_api_version(session, server)

        # verify
        self.assertEqual(result, None)

    @mock.patch('ipa_action.IpaAction._execute')
    def test__get_api_version_bad_ping(self, mock__execute):
        # setup
        action = self.get_action_instance(self.config_blank)

        ping_good = False
        data = {'result': {'summary': "API version 1.234"}}
        mock__execute.return_value = (ping_good, data)

        session = 'session123'
        server = 'server.domain.tld'

        # execute
        result = action._get_api_version(session, server)

        # verify
        self.assertEqual(result, None)

    @mock.patch('ipa_action.IpaAction._execute')
    def test__get_api_version_bad_regex(self, mock__execute):
        # setup
        action = self.get_action_instance(self.config_blank)

        ping_good = True
        data = {'result': {'summary': "API version bad string 1.234"}}
        mock__execute.return_value = (ping_good, data)

        session = 'session123'
        server = 'server.domain.tld'

        # execute
        result = action._get_api_version(session, server)

        # verify
        self.assertEqual(result, None)

    def test_run_login_existing_session(self):
        # setup
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'method': 'login',
                       'session': 'session123',
                       'server': 'server.domain.tld',
                       'username': 'test',
                       'password': 'abc123',
                       'verify_ssl': False}

        # execute
        result = action.run(**kwargs_dict)

        # verify
        self.assertEqual(result, 'session123')
        self.assertEqual(action.session.verify, False)

    @mock.patch('ipa_action.IpaAction._login')
    def test_run_login_missing_session(self, mock__login):
        # setup
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'method': 'login',
                       'server': 'server.domain.tld',
                       'session': None,
                       'username': 'username123',
                       'password': 'password123',
                       'verify_ssl': True}
        mock__login.return_value = 'session123'

        # execute
        result = action.run(**kwargs_dict)

        # verify
        self.assertEqual(result, 'session123')
        self.assertEqual(action.session.verify, True)

    @mock.patch('ipa_action.IpaAction._get_api_version')
    @mock.patch('ipa_action.IpaAction._execute')
    def test_run_execute(self, mock__execute, mock__get_api_version):
        # setup
        action = self.get_action_instance(self.config_blank)
        kwargs = {'method': 'host_add',
                  'session': 'session123',
                  'server': 'server.domain.tld',
                  'username': 'username123',
                  'password': 'password123',
                  'verify_ssl': True}
        mock__get_api_version.return_value = '1.234'
        mock__execute.return_value = (True, {'data': 'value'})

        # execute
        result = action.run(**kwargs)

        # verify
        self.assertEqual(result, (True, {'data': 'value'}))
        self.assertEqual(action.session.verify, True)
        mock__get_api_version.assert_called_with('session123', 'server.domain.tld')
        mock__execute.assert_called_with('session123',
                                         'server.domain.tld',
                                         method='host_add',
                                         api_version='1.234',
                                         username='username123',
                                         password='password123')

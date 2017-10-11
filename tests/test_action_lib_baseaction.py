from freeipa_base_action_test_case import FreeIPABaseActionTestCase
from lib.action import BaseAction, CONFIG_CONNECTION_KEYS

import copy
import mock
import requests


class TestActionLibBaseAction(FreeIPABaseActionTestCase):
    __test__ = True
    action_cls = BaseAction

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, BaseAction)
        self.assertNotEqual(action.session, None)

    def test__get_del_arg_present(self):
        action = self.get_action_instance({})
        test_dict = {"key1": "value1",
                     "key2": "value2"}
        test_key = "key1"
        expected_dict = {"key2": "value2"}
        expected_value = test_dict["key1"]
        result_value = action._get_del_arg(test_key, test_dict)
        self.assertEqual(result_value, expected_value)
        self.assertEqual(test_dict, expected_dict)

    def test__get_del_arg_missing(self):
        action = self.get_action_instance({})
        test_dict = {"key1": "value1",
                     "key2": "value2"}
        test_key = "key3"
        expected_dict = test_dict
        expected_value = None
        result_value = action._get_del_arg(test_key, test_dict)
        self.assertEqual(result_value, expected_value)
        self.assertEqual(test_dict, expected_dict)

    def test__resolve_connection_from_config(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection_config = self.config_good['freeipa'][connection_name]
        connection_expected = {'connection': connection_name}
        connection_expected.update(connection_config)
        kwargs_dict = {'connection': connection_name}
        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_from_config_missing(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'this_connection_doesnt_exist'
        kwargs_dict = {'connection': connection_name}
        with self.assertRaises(KeyError):
            action._resolve_connection(kwargs_dict)

    def test__resolve_connection_from_config_defaults(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection_config = self.config_good['freeipa'][connection_name]
        connection_expected = {'connection': connection_name}
        connection_expected.update(connection_config)
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if not required and default:
                connection_expected[key] = default

        kwargs_dict = {'connection': connection_name}
        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)

    def test__resolve_connection_from_kwargs(self):
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'connection': None,
                       'server': 'kwargs_server',
                       'username': 'kwargs_user',
                       'password': 'kwargs_password'}
        connection_expected = copy.deepcopy(kwargs_dict)
        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, {})

    def test__resolve_connection_from_kwargs_defaults(self):
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'connection': None,
                       'server': 'kwargs_server',
                       'username': 'kwargs_user',
                       'password': 'kwargs_password'}
        connection_expected = copy.deepcopy(kwargs_dict)
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if not required and default:
                connection_expected[key] = default

        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, {})

    def test__resolve_connection_from_kwargs_extras(self):
        action = self.get_action_instance(self.config_blank)
        connection_expected = {'connection': None,
                               'server': 'kwargs_server',
                               'username': 'kwargs_user',
                               'password': 'kwargs_password'}
        kwargs_dict = copy.deepcopy(connection_expected)
        kwargs_extras = {"extra_key1": "extra_value1",
                         "extra_key2": 234}
        kwargs_dict.update(kwargs_extras)
        connection_result = action._resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, kwargs_extras)

    def test__validate_connection(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if required:
                connection[key] = "value_for_key_{}".format(key)

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
        for key, required, default in CONFIG_CONNECTION_KEYS:
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
        connection = self.config_good['freeipa']['base']

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
                                             data=payload,
                                             verify=False)
        self.assertEqual(result, expected_session)

    def test__login_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['freeipa']['base']

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
                                             data=payload,
                                             verify=False)

    def test__login_http_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['freeipa']['base']

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
                                             data=payload,
                                             verify=False)

    def test__execute_success(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['freeipa']['base']

        server = connection['server']
        session = "session123"
        kwargs_dict = {'method': 'host_add',
                       'args': [1, 2, 3],
                       'options': {'a': 'b'}}

        expected_dict = {'result': 'value'}
        expected_result = (True, expected_dict)
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
                   "method": kwargs_dict['method'],
                   "params": [kwargs_dict['args'],
                              kwargs_dict['options']]}

        # execute
        result = action._execute(session, server, kwargs_dict)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             json=payload,
                                             verify=False,
                                             cookies={'ipa_session': session})
        self.assertEqual(result, expected_result)

    def test__execute_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['freeipa']['base']

        server = connection['server']
        session = "session123"
        kwargs_dict = {'method': 'host_add',
                       'args': [1, 2, 3],
                       'options': {'a': 'b'}}

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
                   "method": kwargs_dict['method'],
                   "params": [kwargs_dict['args'],
                              kwargs_dict['options']]}

        # execute
        result = action._execute(session, server, kwargs_dict)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             json=payload,
                                             verify=False,
                                             cookies={'ipa_session': session})
        self.assertEqual(result, expected_result)

    def test__execute_http_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['freeipa']['base']

        server = connection['server']
        session = "session123"
        kwargs_dict = {'method': 'host_add',
                       'args': [1, 2, 3],
                       'options': {'a': 'b'}}

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
                   "method": kwargs_dict['method'],
                   "params": [kwargs_dict['args'],
                              kwargs_dict['options']]}

        # execute
        with self.assertRaises(requests.HTTPError):
            action._execute(session, server, kwargs_dict)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             json=payload,
                                             verify=False,
                                             cookies={'ipa_session': session})

    def test__execute_missing(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['freeipa']['base']

        server = connection['server']
        session = "session123"
        kwargs_dict = {'method': 'host_add'}

        expected_dict = {'result': 'value'}
        expected_result = (True, expected_dict)
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
                   "method": kwargs_dict['method'],
                   "params": [[],   # args
                              {}]}  # options

        # execute
        result = action._execute(session, server, kwargs_dict)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             json=payload,
                                             verify=False,
                                             cookies={'ipa_session': session})
        self.assertEqual(result, expected_result)

    def test__execute_api_version(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection = self.config_good['freeipa']['base']

        server = connection['server']
        session = "session123"
        api_version = "1.234"
        kwargs_dict = {'method': 'host_add',
                       'args': [1, 2, 3],
                       'options': {'a': 'b'}}

        expected_dict = {'result': 'value'}
        expected_result = (True, expected_dict)
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
        expected_options = copy.deepcopy(kwargs_dict)
        expected_options['version'] = api_version
        payload = {"id": 0,
                   "method": kwargs_dict['method'],
                   "params": [kwargs_dict['args'],
                              kwargs_dict['options']]}

        # execute
        result = action._execute(session, server, kwargs_dict, api_version=api_version)

        # verify
        mock_session.post.assert_called_with(url,
                                             headers=headers,
                                             json=payload,
                                             verify=False,
                                             cookies={'ipa_session': session})
        self.assertEqual(result, expected_result)

    @mock.patch('lib.action.BaseAction._execute')
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

    @mock.patch('lib.action.BaseAction._execute')
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

    @mock.patch('lib.action.BaseAction._execute')
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

    @mock.patch('lib.action.BaseAction._execute')
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

    def test_run_existing_session(self):
        # setup
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'method': 'login',
                       'session': 'session123',
                       'server': 'server.domain.tld'}

        # execute
        result = action.run(**kwargs_dict)

        # verify
        self.assertEqual(result, 'session123')

    @mock.patch('lib.action.BaseAction._login')
    def test_run_missing_session(self, mock__login):
        # setup
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'method': 'login',
                       'server': 'server.domain.tld',
                       'username': 'username123',
                       'password': 'password123'}
        mock__login.return_value = 'session123'

        # execute
        result = action.run(**kwargs_dict)

        # verify
        self.assertEqual(result, 'session123')

    @mock.patch('lib.action.BaseAction._get_api_version')
    @mock.patch('lib.action.BaseAction._execute')
    def test_run_execute(self, mock__execute, mock__get_api_version):
        # setup
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'method': 'host_add',
                       'session': 'session123',
                       'server': 'server.domain.tld',
                       'username': 'username123',
                       'password': 'password123'}
        mock__get_api_version.return_value = '1.234'
        mock__execute.return_value = (True, {'data': 'value'})

        # execute
        result = action.run(**kwargs_dict)

        # verify
        self.assertEqual(result, (True, {'data': 'value'}))
        mock__get_api_version.assert_called_with('session123', 'server.domain.tld')
        mock__execute.assert_called_with('session123',
                                         'server.domain.tld',
                                         kwargs_dict,
                                         api_version='1.234')

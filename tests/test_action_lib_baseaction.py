from freeipa_base_action_test_case import FreeIPABaseActionTestCase
from lib.action import BaseAction, CONFIG_CONNECTION_KEYS
import mock
import json
import copy


class TestActionLibBaseAction(FreeIPABaseActionTestCase):
    __test__ = True
    action_cls = BaseAction

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, BaseAction)
        self.assertNotEqual(action.session, None)

    def test_snake_to_camel(self):
        action = self.get_action_instance({})
        snake = "snake_case_string"
        camel = "snakeCaseString"
        result = action.snake_to_camel(snake)
        self.assertEqual(result, camel)

    def test_get_del_arg_present(self):
        action = self.get_action_instance({})
        test_dict = {"key1": "value1",
                     "key2": "value2"}
        test_key = "key1"
        expected_dict = {"key2": "value2"}
        expected_value = test_dict["key1"]
        result_value = action.get_del_arg(test_key, test_dict)
        self.assertEqual(result_value, expected_value)
        self.assertEqual(test_dict, expected_dict)

    def test_get_del_arg_missing(self):
        action = self.get_action_instance({})
        test_dict = {"key1": "value1",
                     "key2": "value2"}
        test_key = "key3"
        expected_dict = test_dict
        expected_value = None
        result_value = action.get_del_arg(test_key, test_dict)
        self.assertEqual(result_value, expected_value)
        self.assertEqual(test_dict, expected_dict)

    def test_resolve_connection_from_config(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection_config = self.config_good['freeipa'][connection_name]
        connection_expected = {'connection': connection_name}
        connection_expected.update(connection_config)
        kwargs_dict = {'connection': connection_name}
        connection_result = action.resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)

    def test_resolve_connection_from_config_missing(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'this_connection_doesnt_exist'
        kwargs_dict = {'connection': connection_name}
        with self.assertRaises(KeyError):
            action.resolve_connection(kwargs_dict)

    def test_resolve_connection_from_config_defaults(self):
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        connection_config = self.config_good['freeipa'][connection_name]
        connection_expected = {'connection': connection_name}
        connection_expected.update(connection_config)
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if not required and default:
                connection_expected[key] = default

        kwargs_dict = {'connection': connection_name}
        connection_result = action.resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)

    def test_resolve_connection_from_kwargs(self):
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'connection': None,
                       'server': 'kwargs_server',
                       'user': 'kwargs_user',
                       'password': 'kwargs_password'}
        connection_expected = copy.deepcopy(kwargs_dict)
        connection_result = action.resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, {})

    def test_resolve_connection_from_kwargs_defaults(self):
        action = self.get_action_instance(self.config_blank)
        kwargs_dict = {'connection': None,
                       'server': 'kwargs_server',
                       'user': 'kwargs_user',
                       'password': 'kwargs_password'}
        connection_expected = copy.deepcopy(kwargs_dict)
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if not required and default:
                connection_expected[key] = default

        connection_result = action.resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, {})

    def test_resolve_connection_from_kwargs_extras(self):
        action = self.get_action_instance(self.config_blank)
        connection_expected = {'connection': None,
                               'server': 'kwargs_server',
                               'user': 'kwargs_user',
                               'password': 'kwargs_password'}
        kwargs_dict = copy.deepcopy(connection_expected)
        kwargs_extras = {"extra_key1": "extra_value1",
                         "extra_key2": 234}
        kwargs_dict.update(kwargs_extras)
        connection_result = action.resolve_connection(kwargs_dict)
        self.assertEqual(connection_result, connection_expected)
        self.assertEqual(kwargs_dict, kwargs_extras)

    def test_validate_connection(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        for key, required, default in CONFIG_CONNECTION_KEYS:
            if required:
                connection[key] = "value_for_key_{}".format(key)

        result = action.validate_connection(connection)
        self.assertTrue(result)

    def test_validate_connection_missing_raises(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        with self.assertRaises(KeyError):
            action.validate_connection(connection)

    def test_validate_connection_none_raises(self):
        action = self.get_action_instance(self.config_blank)
        connection = {}
        for key, required, default in CONFIG_CONNECTION_KEYS:
            connection[key] = None

        with self.assertRaises(KeyError):
            action.validate_connection(connection)

    def test_login_ipa_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        con = self.config_good['freeipa'][connection_name]
        expected_return = mock.Mock(status_code=200)
        mock_session = mock.Mock()
        mock_session.post.return_value = expected_return
        mock_session.post().return_value = mock.Mock(cookies={'ipa_session': ''})
        mock_session.post().cookies = {'sub1': '', 'sub2': ''}
        mock_session.return_value.post().return_value.error = mock.Mock()
        exp_post = mock.Mock(return_value=iter(['error', 'sub1', 'sub2']))
        mock_session.return_value.post.__iter__ = exp_post
        action.session = mock_session
        ipaurl = 'https://{0}/ipa/session/login_password'.format(con['server'])
        login_headers = {"referer": 'https://{0}/ipa/'.format(con['server']),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"}
        payload = 'user={0}&password={1}'.format(con['user'], con['password'])
        # execute
        result = None
        with self.assertRaises(RuntimeError):
            result = action.login(con)
        # verify
        self.assertNotEqual(action.logger.info, None)
        self.assertEqual(result, None)
        mock_session.post.assert_called_with(ipaurl,
        headers=login_headers,
        data=payload,
        verify=False)

    def test_login_ipa_no_error(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection_name = 'base'
        con = self.config_good['freeipa'][connection_name]
        expected_return = mock.Mock(status_code=200)
        mock_session = mock.Mock()
        mock_session.post.return_value = expected_return
        mock_session.post().return_value = mock.Mock(cookies={'ipa_session': ''})
        mock_session.post().cookies = {'ipa_session': '', 'sub1': '', 'sub2': ''}
        mock_session.post().cookies['ipa_session'] = ''
        mock_session.return_value.post().return_value.error = mock.Mock()
        exp_post = mock.Mock(return_value=iter(['sub1', 'sub2']))
        mock_session.return_value.post.__iter__ = exp_post
        action.session = mock_session
        ipaurl = 'https://{0}/ipa/session/login_password'.format(con['server'])
        login_headers = {"referer": 'https://{0}/ipa/'.format(con['server']),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"}
        payload = 'user={0}&password={1}'.format(con['user'], con['password'])
        # execute
        result = action.login(con)
        # verify
        self.assertNotEqual(action.logger.info, None)
        self.assertNotEqual(result[1], None)
        mock_session.post.assert_called_with(ipaurl,
        headers=login_headers,
        data=payload,
        verify=False)
        self.assertEqual(result[0], True)

    def test_make_req(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection_name = 'full'
        con = self.config_good['freeipa'][connection_name]
        expected_return = mock.Mock(status_code=400)
        mock_session = mock.Mock()
        mock_session.post().return_value = expected_return
        mock_session.post().json().return_value = mock.Mock()
        mock_session.post().json().__iter__ = mock.Mock(return_value=iter(['sub1', 'sub2']))
        action.session = mock_session
        json_dict = {'method': con['method'], 'item': [con['args']], 'params': con['params']}
        data = {'id': 0, 'method': json_dict['method'],
        'params': [json_dict['item'], json_dict['params']]}
        ipaurl = 'https://{0}/ipa'.format(con['server'])
        session_url = '{0}/session/json'.format(ipaurl)
        headers = {"referer": 'https://{0}/ipa'.format(con['server']),
        "Content-Type": "application/json",
        "Accept": "application/json"}
        action.server = con['server']
        session = ''
        # execution
        req_made = action.make_req(session, con['server'], json_dict)
        # verify
        mock_session.post.assert_called_with(session_url,
            data=json.dumps(data),
            headers=headers,
            cookies={'ipa_session': session},
            verify=False)
        self.assertEqual(req_made[0], True)
        self.assertNotEqual(req_made[1], None)

    def test_make_req_raised(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection_name = 'full'
        con = self.config_good['freeipa'][connection_name]
        expected_return = mock.Mock(status_code=200)
        mock_session = mock.Mock()
        mock_session.post().return_value = expected_return
        mock_session.post().json().return_value = mock.Mock()
        mock_session.post().json().__iter__ = mock.Mock(return_value=iter(['error', 'sub2']))
        action.session = mock_session
        json_dict = {'method': con['method'], 'item': [con['args']], 'params': con['params']}
        data = {'id': 0, 'method': json_dict['method'],
        'params': [json_dict['item'], json_dict['params']]}
        ipaurl = 'https://{0}/ipa'.format(con['server'])
        session_url = '{0}/session/json'.format(ipaurl)
        headers = {"referer": 'https://{0}/ipa'.format(con['server']),
        "Content-Type": "application/json",
        "Accept": "application/json"}
        action.server = con['server']
        session = ''
        # execution
        req_made = action.make_req(session, con['server'], json_dict)
        # verify
        mock_session.post.assert_called_with(session_url,
            data=json.dumps(data),
            headers=headers,
            cookies={'ipa_session': session},
            verify=False)
        self.assertEqual(req_made[0], False)
        self.assertNotEqual(req_made[1], None)

    def test_run(self):
        # setup
        action = self.get_action_instance(self.config_good)
        connection_name = 'full'
        con = self.config_good['freeipa'][connection_name]
        expected_return = mock.Mock(status_code=200)
        mock_session = mock.Mock()
        mock_session.post().return_value = expected_return
        mock_session.post().json().return_value = mock.Mock()
        mock_session.post().json().__iter__ = mock.Mock(return_value=iter(['sub1', 'sub2']))
        mock_session.post().cookies = {'ipa_session': '', 'sub1': '', 'sub2': ''}
        mock_session.post().cookies['ipa_session'] = ''
        test_dict = {'method': con['method'], 'args': [con['args']],
        'params': con['params'], 'user': con['user'], 'password': con['password'],
        'server': con['server'], 'session': ''}
        action.session = mock_session
        # execution
        req_made = action.run(**test_dict)
        # verify
        self.assertNotEqual(req_made, None)

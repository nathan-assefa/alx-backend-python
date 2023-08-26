#!/usr/bin/env python3
"""
Testing utils script
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    ''' Testing a function that access nested map with key path. '''
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''
        Testing if the nested_map function accesses a a value based on the
        path given in the path parameter
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, exeption):
        '''
        Testing if the nested_map function raises exception if the path is
        wrong using the context manager 'with'
        '''
        with self.assertRaises(exeption):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    Testing a function that handles HTTP requests
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        ''' Mocking(simulating) the requests.get() method '''

        # Create a Mock object for the response from requests.get and
        # + configure its behavior
        mock_response = Mock()

        # Set the return value of the json method of the mock_response
        mock_response.json.return_value = test_payload

        # Set the return value of the whole mock_requests_get
        # + to be the mock_response
        mock_requests_get.return_value = mock_response

        # Call the function being tested
        result = get_json(test_url)

        # Check if requests.get was called with the correct URL
        mock_requests_get.assert_called_once_with(test_url)

        # # Check if the result matches the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    ''' Implementing memoization '''
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        # Create an instance of TestClass
        instance = self.TestClass()

        with patch.object(instance, 'a_method') as mock_a_method:
            # Configure the mock method's return value
            mock_a_method.return_value = 42

            # Call the memoized property twice
            result_1 = instance.a_property
            result_2 = instance.a_property

            # --------> Assertions
            # Ensure a_method is called only once
            mock_a_method.assert_called_once()

            # Check the memoized result
            self.assertEqual(result_1, 42)
            
            # Check the memoized result (should be the same)
            self.assertEqual(result_2, 42)


if __name__ == "__main__":
    unittest.main()

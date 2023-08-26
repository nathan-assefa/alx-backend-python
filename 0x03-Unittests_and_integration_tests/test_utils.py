#!/usr/bin/python3
"""
@parameterized.expand([
    (input_arg1, input_arg2, ..., expected_output1),
    (input_arg1, input_arg2, ..., expected_output2),
    # ... more test cases
])
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
    ********* What is Mock? ***************
    Mocking is primarily about replacing dependencies, not the methods
    themselves. When you're using mocking, you're creating substitute
    objects for the dependencies that a method relies on, allowing you to
    control their ###behavior, responses, and interactions during testing.
    This isolation of dependencies helps you focus solely on testing the
    behavior of the method itself, without worrying about the correctness of
    external systems or making actual network/database calls.

    Example: When we say "mocking" requests.get, we mean that we're creating
    a ----simulated version---- of the #requests.get function that behaves in
    a ----controlled way----. This simulated version, created using the
    unittest.mock library, allows us to define specific behaviors and return
    values that we expect ####---- without actually executing the real
    requests.get function and making actual HTTP calls ----####.


    ********* What is Patch? **************
    The patch context manager is a feature provided by the unittest.mock
    module in Python. It's used to ----temporarily replace---- an object or
    attribute with a mock object, enabling you to ##-----control and manipulate
    the behavior of the object within a specific scope of your code.-----## The
    patch context manager is particularly useful for -----isolating----- and
    -----controlling----- the behavior of ----dependencies---- during testing.
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        ''' Mocking(simulating) the requests.get() method '''

        '''
        **** How patch handles the replacment of requests.get? ****
        The @patch decorator patches the utils.requests.get function, and it's
        passed as the third parameter (mock_requests_get) to the test_get_json
        method. This mock object is created and passed automatically by the
        @patch decorator.
        '''

        # Create a Mock object for the response from requests.get and
        # + configure its behavior
        mock_response = Mock()

        # Set the return value of the json method of the mock_response
        '''
        Configuring the behavior of the --json method-- of the mock_response
        object. The --return_value-- attribute allows you to set what the
        json method should return when it's called. In this case, you're
        setting it to test_payload, which is the JSON data you want to
        simulate as the response content.
        '''
        mock_response.json.return_value = test_payload

        '''
        ********what is return_value?*********
        The value returned when the mock is called.
        '''

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
    '''
    ****** what is memoization? ******
    Memoization is an optimization technique that involves --storing--
    the results of ##expensive function calls and returning the #cached
    result when the same inputs occur again. This helps in avoiding
    redundant computations and improving the performance of functions
    that have heavy computations or repeated calculations.
    '''
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

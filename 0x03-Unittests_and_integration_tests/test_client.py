#!/usr/bin/env python3
''' intracting with github API '''


import unittest
import json
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient 


class TestGithubOrgClient(unittest.TestCase):
    ''' Testing methods of GithubOrgClient '''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        url = test_class.ORG_URL.format(org=input)
        # Assertion
        mock_get_json.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()

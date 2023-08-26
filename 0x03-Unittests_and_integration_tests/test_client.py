#!/usr/bin/env python3
''' intracting with github API '''


import unittest
import json
from unittest.mock import patch, Mock, PropertyMock
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
    
    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url method"""
        @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
        def test_public_repos_url(self, mock_org):
            """ Test that the result of _public_repos_url
            return the correct value based on the given payload
            """
            payload = {"repos_url": "Hello World"}
            mock_org.return_value = payload

            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url

            self.assertEqual(result, payload["repos_url"])

if __name__ == '__main__':
    unittest.main()

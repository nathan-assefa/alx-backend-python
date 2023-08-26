#!/usr/bin/env python3
""" intracting with github API """


import unittest
import json
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing methods of GithubOrgClient"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, input, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        url = test_class.ORG_URL.format(org=input)
        # Assertion
        mock_get_json.assert_called_once_with(url)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that the result of _public_repos_url
        return the correct value based on the given payload
        """
        expected_url = "https://example.com/org/repos"

        # Mock the return value of the property
        mock_org.return_value = {"repos_url": expected_url}

        # Create an instance of GithubOrgClient
        org_client = GithubOrgClient("myorg")

        # Call the _public_repos_url method
        result = org_client._public_repos_url

        # Assertions
        self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()

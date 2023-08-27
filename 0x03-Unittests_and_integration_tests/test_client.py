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

        # Assertion
        self.assertEqual(result, expected_url)

    @patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
            )
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        """
        Test that GithubOrgClient.public_repos returns the
        correct list of repos
        """
        # Mock the return value of _public_repos_url method
        mock_public_repos_url.return_value = "https://example.com/org/repos"

        # Mock the return value of get_json method
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # Create an instance of GithubOrgClient
        org_client = GithubOrgClient("myorg")

        # Call the public_repos method
        result = org_client.public_repos()

        # Assertions
        expected_repos = ["repo1", "repo2", "repo3"]
        self.assertEqual(result, expected_repos)

        # Check if _public_repos_url was called once
        mock_public_repos_url.assert_called_once()

        # Check if get_json was called once with the correct URL
        mock_get_json.assert_called_once_with("https://example.com/org/repos")


if __name__ == "__main__":
    unittest.main()

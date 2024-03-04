import unittest
from unittest.mock import MagicMock as Mock, patch
from api import get_commits_count

class TestInputs(unittest.TestCase):

    @patch('api.requests.get')
    def test_get_commits_count(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'}
        ]
        commits_count = get_commits_count("richkempinski")
        self.assertEqual(commits_count, [('repo1', 2), ('repo2', 2)])

    @patch('api.requests.get')
    def test_get_commits_count_failed_repos(self, mock_get):
        mock_get.return_value.status_code = 404
        commits_count = get_commits_count("richkempinski")
        self.assertEqual(commits_count, "Failed to retrieve repositories. Status code: 404")

if __name__ == '__main__':
    unittest.main()
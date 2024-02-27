import unittest
from api import get_commits_count

class TestInputs(unittest.TestCase):

    def testInvalidInput(self):
        self.assertEqual(get_commits_count(1), "Invalid input. User must be a string.")

    def testInvalidInput(self):
        self.assertEqual(get_commits_count("jgo$&@"), "Invalid input. Github usernames can only contain alphanumeric characters or -'s")
        
    def testGetRepos(self):
        self.assertEqual(get_commits_count("richkempinski"), [('csp', 2), ('hellogitworld', 30), ('helloworld', 6), ('Mocks', 10), ('Project1', 2), ('richkempinski.github.io', 9), ('threads-of-life', 1), ('try_nbdev', 2), ('try_nbdev2', 5)])

    def testGetReposCount(self):
        self.assertEqual(len(get_commits_count("richkempinski")), 9)

    def testGetCommitsCount(self):
        commits_count = get_commits_count("richkempinski")
        for repo, count in commits_count:
            self.assertGreaterEqual(count, 0, f"Invalid commit count for repository {repo}")

if __name__ == '__main__':
    unittest.main()
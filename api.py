import requests

def get_commits_count(user):
    if not isinstance(user, str):
        return "Invalid input. User must be a string."

    # setup the GITHUB URL with the user
    GITHUB_REPOS_URL_WITH_USER = "https://api.github.com/users/{user}/repos"
    GITHUB_COMMITS_URL_WITH_USER_AND_REPO = "https://api.github.com/repos/{user}/{repo}/commits"
    ok_response = 200

    # use requests to call github
    repos = requests.get(GITHUB_REPOS_URL_WITH_USER.format(user=user))

    if repos.status_code == ok_response:
        repos_json = repos.json()
        result = []
        for repo in repos_json:
            repo_name = repo['name']
            commits = requests.get(GITHUB_COMMITS_URL_WITH_USER_AND_REPO.format(user=user, repo=repo_name))
            commits_json = commits.json()
            num_commits = len(commits_json)

            result.append((repo_name, num_commits))

        return result
    else:
        return f"Failed to retrieve repositories. Status code: {repos.status_code}"

print(get_commits_count("richkempinski"))
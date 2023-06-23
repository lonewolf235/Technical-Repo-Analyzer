import requests

def get_user_repositories(username):
    url = "https://api.github.com/users/{}/repos".format(username)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

repositories = get_user_repositories("lonewolf235")

for repository in repositories:
    print(repository["name"])
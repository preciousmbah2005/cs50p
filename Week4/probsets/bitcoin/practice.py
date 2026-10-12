import requests

url = "https://api.github.com/octocat"

try:
    response = requests.get(url)
    print(response.status_code)
    
    content = response.json()
    print(content["login"])
    print(content["public_repos"])
except requests.RequestException as error:
    print(f"Requests failed: {error}")
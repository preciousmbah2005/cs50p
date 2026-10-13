import requests

url = "https://api.github.com/users/octocat"

try:
    response = requests.get(url, timeout=10)
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Body review:", (response.text))

    content = response.json()
    print(content["login"])
    print(content["public_repos"])
except requests.RequestException as error:
    print(f"Requests failed: {error}")
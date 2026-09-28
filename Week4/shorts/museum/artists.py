import requests

def get_artists(query, limit):
    try:
        url = "https://api.artic.edu/api/v1/agents/search"
        response = requests.get(url, {"q": query})
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return[artist["title"] for artist in content["data"]]

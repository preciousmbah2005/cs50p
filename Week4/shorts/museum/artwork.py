import requests

def get_artworks(query, limit):
    try:
        url = "https://api.artic.edu/api/v1/artworks/search"
        response = requests.get(url, {"q": query})
        response.raise_for_status()
    except requests.HTTPError:
        return []

    content = response.json()
    return[artwork["title"] for artwork in content["data"]]

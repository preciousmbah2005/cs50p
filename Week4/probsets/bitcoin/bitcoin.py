import requests
import sys


def main():
    try:
        response = requests.get(
            "https://rest.coincap.io/price/bysymbol",
            {"q": sys.argv}
            )

        content = response.json()
        print(content)
    except requests.RequestException as error:
        print(f"Requests failed: {error}")
        

        
main()

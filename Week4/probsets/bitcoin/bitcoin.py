import requests
import sys

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=dd45cfed6fd8c418a4af8ad557a71d5266068c6aa754bde0b31816e6a7544ced"


try:
    response = requests.get(url)
    response.raise_for_status()

    if len(sys.argv) == 2:
        data = response.json()
        content = float(data["data"]["priceUsd"])
        converting = float(sys.argv[1])
        amount = converting * content
        print(f"${amount:,.4f}")
    elif len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

except requests.RequestException:
    sys.exit()
except ValueError:
    sys.exit("Commmand-line argument is not a number")


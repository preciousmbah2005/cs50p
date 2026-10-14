import requests
import sys

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=dd45cfed6fd8c418a4af8ad557a71d5266068c6aa754bde0b31816e6a7544ced"


try:
    response = requests.get(url)

    if len(sys.argv) == 2:
        data = response.json()
        converting = float(sys.argv[1])
        content = float(data["data"]["priceUsd"])
        amount = converting * content
        print(f"${amount:,.4f}")
    elif len(sys.argv) == 1:
        print("Missing command-line argument")
        
except requests.RequestException:
    print("Error!!")
    sys.exit()
except ValueError:
    print("Commmand-line argument is not a number")


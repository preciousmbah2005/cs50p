import requests
import sys

url = "https://rest.coincap.io/price/bysymbol"

def main():
    try:
        response = requests.get(url)
        if len(sys.argv) == 1:
            content = response.json()
            print(content)
        else:
            sys.exit
            
        
    except requests.RequestException as error:
        print(f"Requests failed: {error}")
    except ValueError:
        print("Command-line argument is not a number")


        

        
main()

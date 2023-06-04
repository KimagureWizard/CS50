import requests
import sys
import json

def main():

    if len(sys.argv) == 2:
        try:
            coin = float(sys.argv[1])
            amount = coin * catch()
            print(f"${amount:,.4f}")
        except (ValueError, IndexError):
            print("Command-line argument is not a number")
            sys.exit
    else:
        print("Missing command-line argument")
        sys.exit


def catch():
    try:
        rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]
        return rate
    except requests.RequestException:
        pass





main()
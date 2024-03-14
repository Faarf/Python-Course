import requests
import sys

if str(sys.argv[1:]).isalpha():
    print("Command-line argument is not a number")
    sys.exit(1)

elif len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)

try:
    input = float(sys.argv[1])
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dict = r.json()
    bitcoin = dict.get("bpi").get("USD").get("rate_float")

except requests.RequestException:
    pass

amount = float(bitcoin) * float(input)

print(f"${amount:,.4f}")

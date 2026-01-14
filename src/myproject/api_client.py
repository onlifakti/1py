import requests

url = "https://zvukipro.com/situacii/941-gromkie-zvuki.html"

r = requests.get(url, timeout=5)

r.raise_for_status()

data = r.json()

print(data["slip"]["advice"])

import json
import requests

url = "https://raw.githubusercontent.com/lavanyadeepak/lavanyadeepak.github.io/refs/heads/master/chants.prod.json"

response = requests.get(url)
response.raise_for_status()  # ensure we got a valid response

data = response.json()  # parse JSON directly

with open("chantsData.js", "w") as f:
    f.write("var chantsData = ")
    json.dump(data, f, indent=2)
    f.write(";")

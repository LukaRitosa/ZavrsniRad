import requests
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

r = requests.get(
    "https://g2-data-api.p.rapidapi.com/g2-products",
    headers={
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "g2-data-api.p.rapidapi.com"
    },
    params={"product": "zoom-workplace", "max_reviews": "50"}
)
data = r.json()
print("Ključevi:", list(data.keys()))
print("Tip reviews:", type(data.get("reviews")))
print(json.dumps(data, indent=2)[:500])
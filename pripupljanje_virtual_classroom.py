import requests
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

url = "https://data.g2.com/api/v2/categories/education" 
api_token = os.getenv("G2_API_TOKEN")

# r = requests.get(
#     "https://data.g2.com/api/v2/categories/31e6a532-241e-4bbb-a192-d2ae057a0d6b",
#     headers={"Authorization": f"Bearer {api_token}"}
# )

# data = r.json()['data']

# # Koliko proizvoda ima u kategoriji?
# products = data['relationships']['products']['data']
# print(f"Broj proizvoda: {len(products)}")
# print("Prvih 5 ID-eva:")
# for p in products[:5]:
#     print(f"  {p['id']}")


'''
090c6f73-9bae-4323-98ac-8880acea7fbd
b587a293-4c04-4ac3-9237-38ad5b96c780
a38250a5-5b8e-4e57-bee2-36c8d155bdd3
87ec9c66-40a3-4dd0-abba-99b5759277fe
4cf7a40d-5310-439c-a53a-ad471153a526
'''

# product_ids = [
#     "090c6f73-9bae-4323-98ac-8880acea7fbd",
#     "b587a293-4c04-4ac3-9237-38ad5b96c780",
#     "a38250a5-5b8e-4e57-bee2-36c8d155bdd3",
#     "87ec9c66-40a3-4dd0-abba-99b5759277fe",
#     "4cf7a40d-5310-439c-a53a-ad471153a526"
# ]

# for pid in product_ids:
#     r = requests.get(
#         f"https://data.g2.com/api/v2/products/{pid}",
#         headers={"Authorization": f"Bearer {api_token}"}
#     )
#     print(r.status_code)
#     print(json.dumps(r.json(), indent=2))
#     print("---")
#     time.sleep(0.5)


r = requests.get(
    "https://data.g2.com/api/v2/snippets",
    headers={"Authorization": f"Bearer {api_token}"},
    params={
        "filter[product_id][]": "090c6f73-9bae-4323-98ac-8880acea7fbd",
        "page[size]": 3
    }
)
print(r.status_code)
print(r.text[:1000])


'''
14 | 31e6a532-241e-4bbb-a192-d2ae057a0d6b | Virtual Classroom | virtual-classroom
'''



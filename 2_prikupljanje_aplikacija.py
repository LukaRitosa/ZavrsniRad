import requests
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

url = "https://data.g2.com/api/v2/categories/education" 
api_token = os.getenv("G2_API_TOKEN")


kategorije = {
    "Virtual Classroom":    "31e6a532-241e-4bbb-a192-d2ae057a0d6b",
    "Assessment":           "32d0a3b1-dc2d-4826-a6eb-d4111cf11f5e",
    "Classroom Management": "5165eab1-0d94-4fe7-9790-1b0f1c00cfc1",
    "Study Tools":          "52d6dac8-a73d-4a9f-97f0-03c044c75745",
    "Classroom Messaging":  "7e81ccb2-7183-4089-9963-59b9c3f21cd0",
    "Tutoring":             "03e6ad15-c113-481d-9b61-99a7a6e12f82"
}

rezultati = {}

for naziv, cat_id in kategorije.items():
    r = requests.get(
        f"https://data.g2.com/api/v2/categories/{cat_id}",
        headers={"Authorization": f"Bearer {api_token}"},
        params={"include": "products"}
    )
    proizvodi = r.json().get("included", [])
    rezultati[naziv] = []
    for p in proizvodi:
        attr = p["attributes"]
        rezultati[naziv].append({
            "name": attr["name"],
            "slug": attr["slug"],
            "rating": attr["star_rating"],
            "reviews": attr["review_count"]
        })
    print(f"\n{naziv}:")
    for p in rezultati[naziv]:
        print(f"  {p['rating']} | {p['reviews']:>6} recenzija | {p['slug']}")
    time.sleep(0.5)


with open("data/kategorije_slugovi.json", "w") as f:
    json.dump(rezultati, f, ensure_ascii=False, indent=2)
print("\nSpravljeno u data/kategorije_slugovi.json")


'''
Virtual Classroom:
  4.5 |  56268 recenzija | zoom-workplace
  4.2 |  18882 recenzija | cisco-webex-suite
  4.0 |    975 recenzija | adobe-connect
  4.4 |    394 recenzija | powerschool-schoology-learning
  4.6 |    852 recenzija | speexx

Assessment:
  4.5 |   1834 recenzija | canvas-lms
  4.6 |    460 recenzija | echo360
  4.6 |    799 recenzija | ispring-suite
  4.6 |    405 recenzija | kahoot
  4.7 |    786 recenzija | mentimeter

Classroom Management:
  4.6 |    517 recenzija | dyknow-classroom
  4.5 |    361 recenzija | classdojo
  4.2 |    116 recenzija | lanschool
  4.6 |    460 recenzija | echo360
  4.8 |    174 recenzija | smart-technologies-lumio

Study Tools:
  4.6 |    405 recenzija | kahoot
  4.6 |    336 recenzija | brainscape
  4.5 |    290 recenzija | quizlet
  4.9 |    256 recenzija | quizizz
  4.7 |    786 recenzija | mentimeter

Classroom Messaging:
  4.8 |    842 recenzija | schoolstatus
  4.8 |    570 recenzija | talkingpoints
  4.6 |    334 recenzija | parentsquare
  4.5 |    361 recenzija | classdojo
  4.4 |    394 recenzija | powerschool-schoology-learning

Tutoring:
  4.2 |    190 recenzija | conexed-conexed
  4.7 |     68 recenzija | vedamo-virtual-classroom
  4.6 |     25 recenzija | yo-coach
  3.2 |     17 recenzija | varsity-tutors
  3.0 |     12 recenzija | tutortrac
'''


'''
14 | 31e6a532-241e-4bbb-a192-d2ae057a0d6b | Virtual Classroom | virtual-classroom
'''



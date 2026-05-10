import requests
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

ALATI = {
    "Virtual Classroom":     ["zoom-workplace", "speexx"],
    "Assessment":            ["echo360", "ispring-suite", "kahoot", "mentimeter"],
    "Classroom Management":  ["dyknow-classroom", "classdojo", "lanschool", "smart-technologies-lumio"],
    "Study Tools":           ["brainscape", "quizlet", "quizizz"],
    "Classroom Messaging":   ["schoolstatus", "talkingpoints", "parentsquare"],
}

def dohvati_alat(slug, kategorija):
    r = requests.get(
        "https://g2-data-api.p.rapidapi.com/g2-products",
        headers={
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "g2-data-api.p.rapidapi.com"
        },
        params={"product": slug, "max_reviews": "50"}
    )
    data = r.json()
    reviews = data.get("all_reviews", [])

    pros, cons = [], []
    ratings = []

    for rev in reviews:
        ratings.append(rev["review_rating"])
        for qa in rev["review_question_answers"]:
            q = qa["question"].lower()
            if "like best" in q:
                pros.append(qa["answer"])
            elif "dislike" in q:
                cons.append(qa["answer"])

    return {
        "name": data.get("product_name", slug),
        "slug": slug,
        "category": kategorija,
        "rating": round(sum(ratings) / len(ratings), 1) if ratings else 0,
        "reviews": len(reviews),
        "pros_raw": pros,
        "cons_raw": cons
    }

os.makedirs("data", exist_ok=True)
rezultati = []

for kategorija, slugovi in ALATI.items():
    for slug in slugovi:
        print(f"Dohvaćam: {slug}...")
        try:
            alat = dohvati_alat(slug, kategorija)
            rezultati.append(alat)
            print(f"  ✓ {alat['name']} | pros: {len(alat['pros_raw'])} | cons: {len(alat['cons_raw'])}")
        except Exception as e:
            print(f"  ✗ Greška za {slug}: {e}")
        time.sleep(1)

with open("data/tools_raw.json", "w", encoding="utf-8") as f:
    json.dump(rezultati, f, ensure_ascii=False, indent=2)

print(f"\n✅ Gotovo — {len(rezultati)} alata → data/tools_raw.json")
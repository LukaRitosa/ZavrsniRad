import requests
from dotenv import load_dotenv
import os
import json
import time
import csv

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

ALATI = {
    "Virtual Classroom":     ["zoom-workplace", "speexx"],
    "Assessment":            ["echo360", "ispring-suite", "kahoot", "mentimeter"],
    "Classroom Management":  ["dyknow-classroom", "classdojo", "lanschool", "smart-technologies-lumio"],
    "Study Tools":           ["brainscape", "quizlet", "quizizz"],
    "Classroom Messaging":   ["schoolstatus", "talkingpoints", "parentsquare"],
}

def izvuci_features(detailed_features):
    """Iz detailed_features izvuci sve feature nazive i postotke kao flat dict."""
    result = {}
    for group in detailed_features:
        group_name = group.get("name", "")
        for feat in group.get("features", []):
            if isinstance(feat, dict) and feat.get("percentage") is not None:
                key = f"{group_name} | {feat['name']}"
                result[key] = {
                    "percentage": feat["percentage"],
                    "based_on": feat.get("based_on_number_of_reviews", 0)
                }
    return result

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
    pros, cons, ratings = [], [], []

    for rev in reviews:
        ratings.append(rev["review_rating"])
        for qa in rev["review_question_answers"]:
            q = qa["question"].lower()
            if "like best" in q:
                pros.append(qa["answer"])
            elif "dislike" in q:
                cons.append(qa["answer"])

    features = izvuci_features(data.get("detailed_features", []))

    return {
        "name": data.get("product_name", slug),
        "slug": slug,
        "category": kategorija,
        "rating": round(sum(ratings) / len(ratings), 1) if ratings else 0,
        "reviews": len(reviews),
        "pros_raw": pros,
        "cons_raw": cons,
        "features": features
    }

os.makedirs("data", exist_ok=True)
rezultati = []

for kategorija, slugovi in ALATI.items():
    for slug in slugovi:
        print(f"Dohvaćam: {slug}...")
        try:
            alat = dohvati_alat(slug, kategorija)
            rezultati.append(alat)
            print(f"  ✓ {alat['name']} | pros: {len(alat['pros_raw'])} | cons: {len(alat['cons_raw'])} | features: {len(alat['features'])}")
        except Exception as e:
            print(f"  ✗ Greška za {slug}: {e}")
        time.sleep(1)


with open("data/tools_raw.json", "w", encoding="utf-8") as f:
    json.dump(rezultati, f, ensure_ascii=False, indent=2)


svi_feature_kljucevi = set()
for alat in rezultati:
    svi_feature_kljucevi.update(alat["features"].keys())
svi_feature_kljucevi = sorted(svi_feature_kljucevi)


with open("data/tools_features.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Header
    writer.writerow(["name", "slug", "category", "rating", "reviews"] + svi_feature_kljucevi)

    for alat in rezultati:
        row = [
            alat["name"],
            alat["slug"],
            alat["category"],
            alat["rating"],
            alat["reviews"],
        ]
        for key in svi_feature_kljucevi:
            feat = alat["features"].get(key)
            row.append(feat["percentage"] if feat else "")
        writer.writerow(row)


with open("data/tools_pros_cons.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "slug", "category", "rating", "reviews", "pros", "cons"])
    for alat in rezultati:
        writer.writerow([
            alat["name"],
            alat["slug"],
            alat["category"],
            alat["rating"],
            alat["reviews"],
            " | ".join(alat["pros_raw"]),
            " | ".join(alat["cons_raw"])
        ])

print(f"\nGotovo — {len(rezultati)} alata")
print(f"   → data/tools_raw.json")
print(f"   → data/tools_features.csv  ({len(svi_feature_kljucevi)} feature stupaca)")
print(f"   → data/tools_pros_cons.csv")
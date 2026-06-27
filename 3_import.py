import requests
from dotenv import load_dotenv
import os
import csv
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

def izvuci_features(detailed_features):
    result = {}
    for group in detailed_features:
        group_name = group.get("name", "")
        for feat in group.get("features", []):
            if isinstance(feat, dict) and feat.get("percentage") is not None:
                key = f"{group_name} | {feat['name']}"
                result[key] = feat["percentage"]
    return result

def dohvati_alat(slug, kategorija):
    r = requests.get(
        "https://g2-data-api.p.rapidapi.com/g2-products",
        headers={
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "g2-data-api.p.rapidapi.com"
        },
        params={"product": slug, "max_reviews": "1"}  
    )
    data = r.json()

    return {
        "name":     data.get("product_name", slug),
        "slug":     slug,
        "category": kategorija,
        "rating":   data.get("rating", 0),
        "features": izvuci_features(data.get("detailed_features", []))
    }


os.makedirs("data", exist_ok=True)
rezultati = []

for kategorija, slugovi in ALATI.items():
    for slug in slugovi:
        print(f"Dohvaćam: {slug}...")
        try:
            alat = dohvati_alat(slug, kategorija)
            rezultati.append(alat)
            print(f"  {alat['name']} | features: {len(alat['features'])}")
        except Exception as e:
            print(f"  ✗ Greška: {e}")
        time.sleep(1)

svi_kljucevi = sorted(set(k for a in rezultati for k in a["features"]))

with open("data/tools_features2.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "slug", "category", "rating"] + svi_kljucevi)
    for alat in rezultati:
        row = [alat["name"], alat["slug"], alat["category"], alat["rating"]]
        row += [alat["features"].get(k, "") for k in svi_kljucevi]
        writer.writerow(row)

print(f"\n{len(rezultati)} alata → data/tools_features2.csv ({len(svi_kljucevi)} feature stupaca)")


'''
Dohvaćam: zoom-workplace...
  Zoom Workplace | features: 157
Dohvaćam: speexx...
  Speexx | features: 48
Dohvaćam: echo360...
  Echo360 | features: 9
Dohvaćam: ispring-suite...
  iSpring Suite | features: 45
Dohvaćam: kahoot...
  Kahoot! | features: 34
Dohvaćam: mentimeter...
  Mentimeter | features: 56
Dohvaćam: dyknow-classroom...
  Dyknow Classroom | features: 7
Dohvaćam: classdojo...
  ClassDojo | features: 18
Dohvaćam: lanschool...
  LanSchool | features: 7
Dohvaćam: smart-technologies-lumio...
  Lumio | features: 22
Dohvaćam: brainscape...
  Brainscape | features: 0
Dohvaćam: quizlet...
  Quizlet | features: 0
Dohvaćam: quizizz...
  Quizizz | features: 4
Dohvaćam: schoolstatus...
  SchoolStatus | features: 8
Dohvaćam: talkingpoints...
  TalkingPoints | features: 8
Dohvaćam: parentsquare...
  ParentSquare | features: 0

16 alata → data/tools_features2.csv (314 feature stupaca)
'''
import pandas as pd
from pathlib import Path

INPUT = Path("data")
OUTPUT = Path("clean_data")

OUTPUT.mkdir(exist_ok=True)

files = [
    "features_classroom_management2.csv",
    "features_assessment2.csv",
    "features_classroom_messaging2.csv",
    "features_virtual_classroom2.csv"
]

osnovni = [
    "name",
    "slug",
    "category",
    "rating",
    "reviews"
]

for file in files:

    path = INPUT / file
    df = pd.read_csv(path)

    print("\n" + "=" * 60)
    print(f"Obrada: {file}")
    
    if "classroom_messaging" in file:

        before = len(df)

        df = df[df["name"] != "ParentSquare"]

        print(
            f"Maknut ParentSquare "
            f"({before} → {len(df)})"
        )
        
    elif "assessment" in file:

        before = len(df)

        # makni Echo360
        df = df[df["name"] != "Echo360"]

        print(
            f"Maknut Echo360 "
            f"({before} → {len(df)} alata)"
        )

        osnovni_postoje = [
            c for c in osnovni
            if c in df.columns
        ]

        feature_cols = [
            c for c in df.columns
            if c not in osnovni_postoje
        ]

        keep = [
            c
            for c in feature_cols
            if df[c].notna().all()
        ]

        df = df[
            osnovni_postoje + keep
        ]

        print(
            f"Ostalo zajedničkih featurea: {len(keep)}"
        )

    out = OUTPUT / file

    df.to_csv(
        out,
        index=False
    )

    print(f"Spremljeno → {out}")

print("\nGotovo.")


'''

============================================================
Obrada: features_classroom_management2.csv
Spremljeno → clean_data\features_classroom_management2.csv

============================================================
Obrada: features_assessment2.csv
Maknut Echo360 (4 → 3 alata)
Ostalo zajedničkih featurea: 7
Featurei:
 - Administration | Mobile compatibility
 - Administration | White-labeling
 - Assessment delivery | Pre-made content
 - Assessment delivery | Question variety
 - Assessment delivery | Real-time assessment
 - Grading and reporting | Analytics dashboard
 - Grading and reporting | Gamification
Spremljeno → clean_data\features_assessment2.csv

============================================================
Obrada: features_classroom_messaging2.csv
Maknut ParentSquare (3 → 2)
Spremljeno → clean_data\features_classroom_messaging2.csv

============================================================
Obrada: features_virtual_classroom2.csv
Spremljeno → clean_data\features_virtual_classroom2.csv

'''
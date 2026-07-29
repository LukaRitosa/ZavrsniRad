# import pandas as pd
# from pathlib import Path

# # INPUT = Path("data")
# INPUT = Path("data2")
# # OUTPUT = Path("clean_data")
# OUTPUT = Path("clean_data2")

# OUTPUT.mkdir(exist_ok=True)

# files = [
#     # "features_classroom_management2.csv",
#     # "features_assessment2.csv",
#     # "features_classroom_messaging2.csv",
#     # "features_virtual_classroom2.csv"
#     "features_virtual_classroom3.csv",
#     "features_classroom_messaging3.csv",
#     "features_classroom_management3.csv",
#     "features_assessment3.csv"
# ]

# osnovni = [
#     "name",
#     "slug",
#     "category",
#     "rating",
#     "reviews"
# ]

# for file in files:

#     path = INPUT / file
#     df = pd.read_csv(path)

#     print("\n" + "=" * 60)
#     print(f"Obrada: {file}")
    
#     if "classroom_messaging" in file:

#         before = len(df)

#         df = df[df["name"] != "ParentSquare"]

#         print(
#             f"Maknut ParentSquare "
#             f"({before} → {len(df)})"
#         )

#     elif "virtual_classroom" in file:

#         before = len(df)

#         df = df[df["slug"] != "powerschool-schoology-learning"]

#         print(
#             f"Maknut PowerSchool Schoology Learning "
#             f"({before} → {len(df)} alata)"
#         )
        
#     elif "assessment" in file:

#         before = len(df)

#         df = df[df["name"] != "Echo360"]

#         print(
#             f"Maknut Echo360 "
#             f"({before} → {len(df)} alata)"
#         )

#         osnovni_postoje = [
#             c for c in osnovni
#             if c in df.columns
#         ]

#         feature_cols = [
#             c for c in df.columns
#             if c not in osnovni_postoje
#         ]

#         keep = [
#             c
#             for c in feature_cols
#             if df[c].notna().all()
#         ]

#         df = df[
#             osnovni_postoje + keep
#         ]

#         print(
#             f"Ostalo zajedničkih featurea: {len(keep)}"
#         )

#     out = OUTPUT / file

#     df.to_csv(
#         out,
#         index=False
#     )

#     print(f"Spremljeno → {out}")

# print("\nGotovo.")


import pandas as pd

input_file = "data2/features_virtual_classroom3.csv"
output_file = "clean_data2/features_virtual_classroom3.csv"

df = pd.read_csv(input_file)

print(f"Početni broj alata: {len(df)}")

df = df[df["slug"] != "powerschool-schoology-learning"]

print(f"Nakon micanja PowerSchoola: {len(df)} alata")

osnovni = ["name", "slug", "category", "rating", "reviews"]
osnovni = [c for c in osnovni if c in df.columns]

feature_cols = [c for c in df.columns if c not in osnovni]

zajednicki = [c for c in feature_cols if df[c].notna().all()]

print(f"\nZajedničkih featurea: {len(zajednicki)}")

for feat in zajednicki:
    print("•", feat)

df = df[osnovni + zajednicki]
df.to_csv(output_file, index=False)

print(f"\nSpremljeno u: {output_file}")

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




============================================================
Obrada: features_virtual_classroom3.csv
Maknut PowerSchool Schoology Learning (5 → 4 alata)
Spremljeno → clean_data2\features_virtual_classroom3.csv

============================================================
Obrada: features_classroom_messaging3.csv
Maknut ParentSquare (3 → 3)
Spremljeno → clean_data2\features_classroom_messaging3.csv

============================================================
Obrada: features_classroom_management3.csv
Spremljeno → clean_data2\features_classroom_management3.csv

============================================================
Obrada: features_assessment3.csv
Maknut Echo360 (4 → 3 alata)
Ostalo zajedničkih featurea: 7
Spremljeno → clean_data2\features_assessment3.csv
'''
import pandas as pd

files = [
    "data2/features_virtual_classroom3.csv"
]

for file in files:
    print("\n" + "=" * 80)

    df = pd.read_csv(file)

    df = df[df["slug"] != "powerschool-schoology-learning"]

    kategorija = df["category"].iloc[0]

    osnovni = ["name", "slug", "category", "rating", "reviews"]
    feature_cols = [c for c in df.columns if c not in osnovni]

    zajednicki = []

    for col in feature_cols:
        if df[col].notna().all():
            zajednicki.append(col)

    print(f"Kategorija: {kategorija}")
    print(f"Broj zajedničkih featurea: {len(zajednicki)}\n")

    for feat in zajednicki:
        print("•", feat)


'''
================================================================================
Kategorija: Virtual Classroom
Broj zajedničkih featurea: 11

• Collaboration | Hand Raising
• Collaboration | Participation Controls
• Collaboration | Screen Sharing
• Collaboration | Survey Tools
• Collaboration | Whiteboard
• Content Sharing | File Sharing
• Content Sharing | Session Recording
• Content Sharing | Video Streaming
• Functionality | Live Chat
• Functionality | Markup Tools
• Functionality | Technical Support
'''
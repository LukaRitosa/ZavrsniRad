import pandas as pd
from pathlib import Path

INPUT = Path("clean_data2")
OUTPUT = Path("data_hr")

OUTPUT.mkdir(exist_ok=True)

translations = {
    "features_virtual_classroom3.csv": {
        "Collaboration | Hand Raising":
            "Dizanje ruke",

        "Collaboration | Participation Controls":
            "Upravljanje sudjelovanjem",

        "Collaboration | Screen Sharing":
            "Dijeljenje zaslona",

        "Collaboration | Survey Tools":
            "Alati za ankete",

        "Collaboration | Whiteboard":
            "Digitalna ploča",

        "Content Sharing | File Sharing":
            "Dijeljenje datoteka",

        "Content Sharing | Session Recording":
            "Snimanje sastanka/nastave",

        "Content Sharing | Video Streaming":
            "Prijenos videa uživo",

        "Functionality | Live Chat":
            "Slanje poruka",

        "Functionality | Markup Tools":
            "Alati za označavanje",

        "Functionality | Technical Support":
            "Tehnička podrška",
    }
}

category_translation = {
    "Virtual Classroom": "Virtualna učionica",
}

for filename, mapping in translations.items():

    path = INPUT / filename

    if not path.exists():
        print(f"Preskačem: {filename}")
        continue

    df = pd.read_csv(path)

    if "category" in df.columns:
        df["category"] = df["category"].replace(category_translation)

    df = df.rename(columns=mapping)

    output_path = OUTPUT / filename

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"Spremljeno → {output_path}")

print("\nGotovo.")
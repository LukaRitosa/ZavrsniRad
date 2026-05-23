import pandas as pd

df = pd.read_csv("data/tools_features.csv")
df = df[df["reviews"] > 0]

kategorije = df["category"].unique()

for kat in kategorije:
    df_kat = df[df["category"] == kat].copy()
    
    
    cols_osnovni = ["name", "slug", "category", "rating", "reviews"]
    cols_features = [c for c in df_kat.columns[5:] 
                     if df_kat[c].notna().all()]
    
    if not cols_features:
        
        cols_features = [c for c in df_kat.columns[5:] 
                         if df_kat[c].notna().any()]
        print(f"\n⚠️  {kat} — nema stupaca gdje SVI imaju vrijednost, koristim gdje barem jedan ima ({len(cols_features)} stupaca)")
    else:
        print(f"\n✓  {kat} — {len(cols_features)} zajedničkih feature stupaca")

    df_out = df_kat[cols_osnovni + cols_features]
    
    
    for col in cols_features:
        vals = df_out[col].dropna().tolist()
        print(f"     {col}: {vals}")
    
    filename = f"data/features_{kat.lower().replace(' ', '_')}.csv"
    df_out.to_csv(filename, index=False)
    print(f"     → {filename}")
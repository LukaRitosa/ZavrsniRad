import pandas as pd

df = pd.read_csv("data/tools_features2.csv")
# df = df[df["reviews"] > 0]


min_alata = 4
cols_osnovni = ["name", "slug", "category", "rating"]
cols_features = [c for c in df.columns[5:] if df[c].notna().sum() >= min_alata]

df_clean = df[cols_osnovni + cols_features]

print(f"Alata: {len(df_clean)}")
print(f"Feature stupaca: {len(cols_features)}")
print("\nStupci i koliko alata ih ima:")
for col in cols_features:
    n = df_clean[col].notna().sum()
    print(f"  {n:>2} alata | {col}")

df_clean.to_csv("data/tools_clean2.csv", index=False)
print("\n✅ → data/tools_clean2.csv")

'''
Alata: 16
Feature stupaca: 15

Stupci i koliko alata ih ima:
   4 alata | Administration | Mobile compatibility
   4 alata | Administration | White-labeling
   4 alata | Assessment delivery | Pre-made content
   4 alata | Assessment delivery | Question variety
   4 alata | Assessment delivery | Real-time assessment
   4 alata | Audience Engagement | Quizzes
   4 alata | Engagement Analytics | Dashboards & Reporting
   4 alata | Engagement Analytics | Live Results
   4 alata | Grading and reporting | Analytics dashboard
   4 alata | Grading and reporting | Gamification
   4 alata | Platform Features | Instant Messaging
   4 alata | Platform Features | Interactive Quizzes
   4 alata | Platform Features | Remote Computer Monitoring
   4 alata | Platform Features | Student Assignment Distribution
   4 alata | Platform Features | Teacher/Student Screensharing

✅ → data/tools_clean2.csv    
'''
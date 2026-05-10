

SVI_ALATI = {
    "Virtual Classroom": [
        "zoom-workplace",       # 4.5 | 56268
        "speexx",               # 4.6 | 852
    ],
    "Assessment": [
        "echo360",              # 4.6 | 460
        "ispring-suite",        # 4.6 | 799
        "kahoot",               # 4.6 | 405
        "mentimeter",           # 4.7 | 786
    ],
    "Classroom Management": [
        "dyknow-classroom",         # 4.6 | 517
        "classdojo",                # 4.5 | 361
        "lanschool",                # 4.2 | 116
        "smart-technologies-lumio", # 4.8 | 174
    ],
    "Study Tools": [
        "brainscape",           # 4.6 | 336
        "quizlet",              # 4.5 | 290
        "quizizz",              # 4.9 | 256
    ],
    "Classroom Messaging": [
        "schoolstatus",         # 4.8 | 842
        "talkingpoints",        # 4.8 | 570
        "parentsquare",         # 4.6 | 334
    ],
}

filtrirani = {
    slug: info for slug, info in SVI_ALATI.items()
    if info["rating"] >= 4.0 and info["reviews"] >= 100
}

print(f"Ukupno alata: {len(filtrirani)}\n")
for slug, info in filtrirani.items():
    print(f"  {info['rating']} | {info['reviews']:>6} | {info['cat']:<25} | {slug}")
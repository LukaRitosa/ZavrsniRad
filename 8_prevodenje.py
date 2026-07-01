
'''
clean_data/features_assessment2.csv


Administration | Mobile compatibility - Prilagođeno mobilnim uređajima
Administration | White-labeling - Prilagodba izgleda
Assessment delivery | Pre-made content - Gotovi sadržaji
Assessment delivery | Question variety - Raznolikost vrsta pitanja
Assessment delivery | Real-time assessment - Procjena u stvarnom vremenu
Grading and reporting | Analytics dashboard - Analitika
Grading and reporting | Gamification - Elementi igre



clean_data/features_classroom_management2.csv


Platform Features | Instant Messaging - Razmjena poruka u stvarnom vremenu 
Platform Features | Interactive Quizzes - Interaktivni kvizovi
Platform Features | Remote Computer Monitoring - Praćenja rada
Platform Features | Student Assignment Distribution - Dodjela zadataka
Platform Features | Teacher/Student Screensharing - Djeljenje zaslona



clean_data/features_classroom_messaging2.csv - obrisati



Functionality | Analytics - Analitika - x
Functionality | Mass Messaging - Skupno slanje poruka
Functionality | Multimedia - Mutimedijski sadržaji
Functionality | Push Notifications - Obavijesti
Functionality | Student Messaging - Komunikacija s učenicima
Integration | Classroom Management - x
Integration | LMS Integration - x
Integration | Message Sync - x


clean_data/features_virtual_classroom2.csv

Collaboration | Hand Raising - Dizanje ruke
Collaboration | Participation Controls - Upravljanje sudjelovanjem
Collaboration | Screen Sharing - Dijeljenje zaslona
Collaboration | Survey Tools - Alati za ankete
Collaboration | Whiteboard - Digitalna ploča
Content Sharing | File Sharing - Dijeljenje datoteka
Content Sharing | Session Recording - Snimanje sastanka/nastave
Content Sharing | Video Streaming - Prijenos videa uživo 
Functionality | Live Chat - Slanje poruka
Functionality | Markup Tools - Alati za označavanje
Functionality | Technical Support - Tehnička podrška

'''


import pandas as pd
from pathlib import Path

INPUT = Path("clean_data")
OUTPUT = Path("data_hr")

OUTPUT.mkdir(exist_ok=True)

translations = {
    "features_assessment2.csv": {
        "Administration | Mobile compatibility":
            "Prilagođeno mobilnim uređajima",

        "Administration | White-labeling":
            "Prilagodba izgleda",

        "Assessment delivery | Pre-made content":
            "Gotovi sadržaji",

        "Assessment delivery | Question variety":
            "Raznolikost vrsta pitanja",

        "Assessment delivery | Real-time assessment":
            "Procjena u stvarnom vremenu",

        "Grading and reporting | Analytics dashboard":
            "Analitika",

        "Grading and reporting | Gamification":
            "Elementi igre",
    },

    "features_classroom_management2.csv": {
        "Platform Features | Instant Messaging":
            "Razmjena poruka u stvarnom vremenu",

        "Platform Features | Interactive Quizzes":
            "Interaktivni kvizovi",

        "Platform Features | Remote Computer Monitoring":
            "Praćenja rada",

        "Platform Features | Student Assignment Distribution":
            "Dodjela zadataka",

        "Platform Features | Teacher/Student Screensharing":
            "Djeljenje zaslona",
    },

    "features_virtual_classroom2.csv": {
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

for filename, mapping in translations.items():

    path = INPUT / filename

    if not path.exists():
        print(f"Preskačem: {filename}")
        continue

    df = pd.read_csv(path)

    df = df.rename(columns=mapping)

    output_path = OUTPUT / filename

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"Spremljeno → {output_path}")

print("\nGotovo.")
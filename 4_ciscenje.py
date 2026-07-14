import pandas as pd

df = pd.read_csv("data/tools_features2.csv")
# df = df[df["reviews"] > 0]

kategorije = df["category"].unique()

for kat in kategorije:
    df_kat = df[df["category"] == kat].copy()
    
    
    cols_osnovni = ["name", "slug", "category", "rating"]
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
    
    filename = f"data/features_{kat.lower().replace(' ', '_')}2.csv"
    df_out.to_csv(filename, index=False)
    print(f"     → {filename}")


    '''
✓  Virtual Classroom — 11 zajedničkih feature stupaca
     Collaboration | Hand Raising: [91.0, 88.0]
     Collaboration | Participation Controls: [90.0, 89.0]
     Collaboration | Screen Sharing: [93.0, 88.0]
     Collaboration | Survey Tools: [87.0, 86.0]
     Collaboration | Whiteboard: [86.0, 86.0]
     Content Sharing | File Sharing: [88.0, 88.0]
     Content Sharing | Session Recording: [91.0, 84.0]
     Content Sharing | Video Streaming: [90.0, 88.0]
     Functionality | Live Chat: [90.0, 89.0]
     Functionality | Markup Tools: [87.0, 86.0]
     Functionality | Technical Support: [86.0, 88.0]
     → data/features_virtual_classroom2.csv

⚠️  Assessment — nema stupaca gdje SVI imaju vrijednost, koristim gdje barem jedan ima (96 stupaca)
     Account Options | Bookmarking: [69.0]
     Account Options | History: [73.0]
     Account Options | Reputation System: [70.0]
     Account Options | Single Sign-On (SSO): [85.0]
     Account Options | Social Login: [74.0]
     Account Options | Topic Subscription: [66.0]
     Additional Features- | Analytics: [80.0]
     Additional Features- | Educational: [81.0]
     Additional Features- | Virtual Office: [72.0]
     Administration | Mobile compatibility: [84.0, 93.0, 92.0]
     Administration | White-labeling: [87.0, 77.0, 77.0]
     Assessment delivery | Pre-made content: [83.0, 88.0, 82.0]
     Assessment delivery | Question variety: [90.0, 90.0, 88.0]
     Assessment delivery | Real-time assessment: [86.0, 96.0, 95.0]
     Audience Engagement | Audience Q&A: [92.0, 94.0, 92.0]
     Audience Engagement | Live Slides: [91.0, 90.0]
     Audience Engagement | Polls and Surveys: [93.0, 93.0, 94.0]
     Audience Engagement | Quizzes: [88.0, 97.0, 92.0]
     Basics | Mobility: [93.0]
     Basics | Performance: [92.0]
     Content | Content Creation: [91.0]
     Content | Content Library: [90.0]
     Content | Customizability: [91.0]
     Core Features | Connection: [86.0]
     Core Features | Creative: [85.0]
     Core Features | Gamification: [83.0]
     Core Features | Reports: [83.0]
     Course Authoring | Assessments & Quizzes: [90.0]
     Course Authoring | Course Builder: [90.0]
     Course Delivery | 24/7 Availability: [90.0]
     Course Delivery | Learning Paths: [83.0]
     Course Management | Certifications: [83.0]
     Course Management | Industry Compliance: [85.0]
     Engagement Analytics | Dashboards & Reporting: [78.0, 93.0, 88.0]
     Engagement Analytics | Data Exporting: [82.0, 91.0, 87.0]
     Engagement Analytics | Live Results: [94.0, 96.0, 95.0]
     Event Support | Event Security: [85.0, 91.0]
     Event Support | Hybrid/Virtual Events: [91.0, 87.0]
     Event Support | Integrations: [88.0, 86.0, 80.0]
     Event Support | SMS Voting: [91.0]
     Generative AI | AI Image-to-Text: [59.0]
     Generative AI | AI Text Generation: [77.0]
     Generative AI | AI Text Summarization: [53.0, 72.0]
     Generative AI | AI Text-to-Image: [53.0]
     Generative AI | AI Text-to-Music: [56.0]
     Generative AI | AI Text-to-Speech: [68.0]
     Generative AI | AI Text-to-Video: [51.0]
     Grading and reporting | Analytics dashboard: [77.0, 91.0, 86.0]
     Grading and reporting | Automated grading: [90.0, 97.0]
     Grading and reporting | Gamification: [79.0, 96.0, 86.0]
     Grading and reporting | Reporting: [80.0, 90.0]
     Interface | Multilingual: [82.0]
     Interface | White Labeling: [81.0]
     Interoperability | Images or Gifs: [81.0]
     Interoperability | Integration: [76.0]
     Interoperability | Recognition & Rewards: [69.0]
     Performance | Interoperability: [91.0]
     Performance | Monitoring: [92.0]
     Performance | Reporting: [91.0]
     Planning | Collaborative Editorial Calendars / Scheduling Content: [59.0]
     Planning | Scheduling Integration: [61.0]
     Platform Additional Functionality | Cloud: [86.0, 85.0]
     Platform Additional Functionality | Messaging: [68.0]
     Platform Additional Functionality | Mobility: [81.0]
     Platform Basics | Auto Save: [87.0, 93.0]
     Platform Basics | Presenter Tools: [90.0, 86.0]
     Platform Basics | Slide Design: [89.0, 82.0]
     Platform Content | Charts: [89.0, 87.0]
     Platform Content | File Sharing: [79.0, 81.0]
     Platform Content | Template Creator: [87.0, 82.0]
     Platform Content | Template Library: [86.0, 82.0]
     Publishing | Execute Content Publication: [88.0]
     Q&A Tools | Analytics: [78.0]
     Q&A Tools | Commenting System: [75.0]
     Q&A Tools | Embedding: [74.0]
     Q&A Tools | Formatting: [75.0]
     Q&A Tools | Integrations: [73.0]
     Q&A Tools | Knowledge Integrations: [75.0]
     Q&A Tools | Notifications: [73.0]
     Q&A Tools | Tags: [77.0]
     Q&A Tools | Voting: [85.0]
     Social Media | Social Media Integration: [63.0]
     Survey Customization | Branding: [84.0]
     Survey Customization | Multilingual Surveys: [79.0]
     Survey Customization | Multimedia Support: [83.0]
     Survey Insights | Data Exporting: [83.0]
     Survey Insights | Permissions: [82.0]
     Survey Management | Question Types: [90.0]
     Survey Management | Templates: [85.0]
     Training & eLearning | Assessments and Practice: [89.0, 93.0]
     Training & eLearning | Content Creation: [91.0, 91.0]
     Training & eLearning | Content Delivery and Tracking: [85.0, 93.0]
     Training & eLearning | Content Libraries: [82.0, 90.0]
     Training & eLearning | Content Storage and Management: [85.0, 91.0]
     Training & eLearning | Customer Training: [85.0]
     Training & eLearning | Manager Portals: [81.0, 90.0]
     → data/features_assessment2.csv

✓  Classroom Management — 5 zajedničkih feature stupaca
     Platform Features | Instant Messaging: [90.0, 92.0, 84.0, 81.0]
     Platform Features | Interactive Quizzes: [81.0, 74.0, 78.0, 92.0]
     Platform Features | Remote Computer Monitoring: [97.0, 86.0, 87.0, 89.0]
     Platform Features | Student Assignment Distribution: [82.0, 82.0, 81.0, 93.0]
     Platform Features | Teacher/Student Screensharing: [88.0, 85.0, 88.0, 94.0]
     → data/features_classroom_management2.csv

⚠️  Study Tools — nema stupaca gdje SVI imaju vrijednost, koristim gdje barem jedan ima (4 stupaca)
     Audience Engagement | Quizzes: [88.0]
     Engagement Analytics | Dashboards & Reporting: [90.0]
     Engagement Analytics | Live Results: [95.0]
     Event Support | Hybrid/Virtual Events: [95.0]
     → data/features_study_tools2.csv

⚠️  Classroom Messaging — nema stupaca gdje SVI imaju vrijednost, koristim gdje barem jedan ima (8 stupaca)
     Functionality | Analytics: [94.0, 92.0]
     Functionality | Mass Messaging: [96.0, 97.0]
     Functionality | Multimedia: [91.0, 90.0]
     Functionality | Push Notifications: [93.0, 93.0]
     Functionality | Student Messaging: [89.0, 94.0]
     Integration | Classroom Management: [95.0, 94.0]
     Integration | LMS Integration: [91.0, 93.0]
     Integration | Message Sync: [94.0, 94.0]
     → data/features_classroom_messaging2.csv
    '''
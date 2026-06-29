import pandas as pd
from pathlib import Path

files = [
    "data/features_classroom_management2.csv",
    "data/features_assessment2.csv",
    "data/features_classroom_messaging2.csv",
    "data/features_study_tools2.csv",
    "data/features_virtual_classroom2.csv"
]

for file in files:
    print("\n" + "="*80)
    df = pd.read_csv(file)
    
    kategorija = df["category"].iloc[0]
    alati = df["name"].tolist()
    
    osnovni = ["name", "slug", "category", "rating", "reviews"]
    feature_cols = [c for c in df.columns if c not in osnovni]
    
    print(f"{kategorija}")
    print(f"{'Kriterij':<50} " + "  ".join(f"{a:<20}" for a in alati))
    print("-" * (50 + 22 * len(alati)))
    
    for col in feature_cols:
        ima = []
        for _, row in df.iterrows():
            if pd.notna(row[col]):
                ima.append("✅")
            else:
                ima.append("❌")
        print(f"{col:<50} " + "  ".join(f"{v:<20}" for v in ima))



'''

================================================================================
Classroom Management
Kriterij                                           Dyknow Classroom      ClassDojo             LanSchool             Lumio               
------------------------------------------------------------------------------------------------------------------------------------------
Platform Features | Instant Messaging              ✅                     ✅                     ✅                     ✅                   
Platform Features | Interactive Quizzes            ✅                     ✅                     ✅                     ✅                   
Platform Features | Remote Computer Monitoring     ✅                     ✅                     ✅                     ✅                   
Platform Features | Student Assignment Distribution ✅                     ✅                     ✅                     ✅                   
Platform Features | Teacher/Student Screensharing  ✅                     ✅                     ✅                     ✅                   

================================================================================
Assessment
Kriterij                                           Echo360               iSpring Suite         Kahoot!               Mentimeter          
------------------------------------------------------------------------------------------------------------------------------------------
Account Options | Bookmarking                      ❌                     ❌                     ❌                     ✅                   
Account Options | History                          ❌                     ❌                     ❌                     ✅                   
Account Options | Reputation System                ❌                     ❌                     ❌                     ✅                   
Account Options | Single Sign-On (SSO)             ❌                     ❌                     ❌                     ✅                   
Account Options | Social Login                     ❌                     ❌                     ❌                     ✅                   
Account Options | Topic Subscription               ❌                     ❌                     ❌                     ✅                   
Additional Features- | Analytics                   ❌                     ❌                     ❌                     ✅                   
Additional Features- | Educational                 ❌                     ❌                     ❌                     ✅                   
Additional Features- | Virtual Office              ❌                     ❌                     ❌                     ✅                   
Administration | Mobile compatibility              ❌                     ✅                     ✅                     ✅                   
Administration | White-labeling                    ❌                     ✅                     ✅                     ✅                   
Assessment delivery | Pre-made content             ❌                     ✅                     ✅                     ✅                   
Assessment delivery | Question variety             ❌                     ✅                     ✅                     ✅                   
Assessment delivery | Real-time assessment         ❌                     ✅                     ✅                     ✅                   
Audience Engagement | Audience Q&A                 ✅                     ❌                     ✅                     ✅                   
Audience Engagement | Live Slides                  ✅                     ❌                     ✅                     ❌                   
Audience Engagement | Polls and Surveys            ✅                     ❌                     ✅                     ✅                   
Audience Engagement | Quizzes                      ✅                     ❌                     ✅                     ✅                   
Basics | Mobility                                  ❌                     ❌                     ✅                     ❌                   
Basics | Performance                               ❌                     ❌                     ✅                     ❌                   
Content | Content Creation                         ❌                     ❌                     ✅                     ❌                   
Content | Content Library                          ❌                     ❌                     ✅                     ❌                   
Content | Customizability                          ❌                     ❌                     ✅                     ❌                   
Core Features | Connection                         ❌                     ❌                     ❌                     ✅                   
Core Features | Creative                           ❌                     ❌                     ❌                     ✅                   
Core Features | Gamification                       ❌                     ❌                     ❌                     ✅                   
Core Features | Reports                            ❌                     ❌                     ❌                     ✅                   
Course Authoring | Assessments & Quizzes           ❌                     ✅                     ❌                     ❌                   
Course Authoring | Course Builder                  ❌                     ✅                     ❌                     ❌                   
Course Delivery | 24/7 Availability                ❌                     ✅                     ❌                     ❌                   
Course Delivery | Learning Paths                   ❌                     ✅                     ❌                     ❌                   
Course Management | Certifications                 ❌                     ✅                     ❌                     ❌                   
Course Management | Industry Compliance            ❌                     ✅                     ❌                     ❌                   
Engagement Analytics | Dashboards & Reporting      ✅                     ❌                     ✅                     ✅                   
Engagement Analytics | Data Exporting              ✅                     ❌                     ✅                     ✅                   
Engagement Analytics | Live Results                ✅                     ❌                     ✅                     ✅                   
Event Support | Event Security                     ✅                     ❌                     ✅                     ❌                   
Event Support | Hybrid/Virtual Events              ❌                     ❌                     ✅                     ✅                   
Event Support | Integrations                       ✅                     ❌                     ✅                     ✅                   
Event Support | SMS Voting                         ❌                     ❌                     ✅                     ❌                   
Generative AI | AI Image-to-Text                   ❌                     ✅                     ❌                     ❌                   
Generative AI | AI Text Generation                 ❌                     ✅                     ❌                     ❌                   
Generative AI | AI Text Summarization              ❌                     ✅                     ❌                     ✅                   
Generative AI | AI Text-to-Image                   ❌                     ✅                     ❌                     ❌                   
Generative AI | AI Text-to-Music                   ❌                     ✅                     ❌                     ❌                   
Generative AI | AI Text-to-Speech                  ❌                     ✅                     ❌                     ❌                   
Generative AI | AI Text-to-Video                   ❌                     ✅                     ❌                     ❌                   
Grading and reporting | Analytics dashboard        ❌                     ✅                     ✅                     ✅                   
Grading and reporting | Automated grading          ❌                     ✅                     ✅                     ❌                   
Grading and reporting | Gamification               ❌                     ✅                     ✅                     ✅                   
Grading and reporting | Reporting                  ❌                     ✅                     ✅                     ❌                   
Interface | Multilingual                           ❌                     ✅                     ❌                     ❌                   
Interface | White Labeling                         ❌                     ✅                     ❌                     ❌                   
Interoperability | Images or Gifs                  ❌                     ❌                     ❌                     ✅                   
Interoperability | Integration                     ❌                     ❌                     ❌                     ✅                   
Interoperability | Recognition & Rewards           ❌                     ❌                     ❌                     ✅                   
Performance | Interoperability                     ❌                     ❌                     ✅                     ❌                   
Performance | Monitoring                           ❌                     ❌                     ✅                     ❌                   
Performance | Reporting                            ❌                     ❌                     ✅                     ❌                   
Planning | Collaborative Editorial Calendars / Scheduling Content ❌                     ✅                     ❌                     ❌                   
Planning | Scheduling Integration                  ❌                     ✅                     ❌                     ❌                   
Platform Additional Functionality | Cloud          ❌                     ✅                     ❌                     ✅                   
Platform Additional Functionality | Messaging      ❌                     ✅                     ❌                     ❌                   
Platform Additional Functionality | Mobility       ❌                     ✅                     ❌                     ❌                   
Platform Basics | Auto Save                        ❌                     ✅                     ❌                     ✅                   
Platform Basics | Presenter Tools                  ❌                     ✅                     ❌                     ✅                   
Platform Basics | Slide Design                     ❌                     ✅                     ❌                     ✅                   
Platform Content | Charts                          ❌                     ✅                     ❌                     ✅                   
Platform Content | File Sharing                    ❌                     ✅                     ❌                     ✅                   
Platform Content | Template Creator                ❌                     ✅                     ❌                     ✅                   
Platform Content | Template Library                ❌                     ✅                     ❌                     ✅                   
Publishing | Execute Content Publication           ❌                     ✅                     ❌                     ❌                   
Q&A Tools | Analytics                              ❌                     ❌                     ❌                     ✅                   
Q&A Tools | Commenting System                      ❌                     ❌                     ❌                     ✅                   
Q&A Tools | Embedding                              ❌                     ❌                     ❌                     ✅                   
Q&A Tools | Formatting                             ❌                     ❌                     ❌                     ✅                   
Q&A Tools | Integrations                           ❌                     ❌                     ❌                     ✅                   
Q&A Tools | Knowledge Integrations                 ❌                     ❌                     ❌                     ✅                   
Q&A Tools | Notifications                          ❌                     ❌                     ❌                     ✅                   
Q&A Tools | Tags                                   ❌                     ❌                     ❌                     ✅                   
Q&A Tools | Voting                                 ❌                     ❌                     ❌                     ✅                   
Social Media | Social Media Integration            ❌                     ✅                     ❌                     ❌                   
Survey Customization | Branding                    ❌                     ❌                     ❌                     ✅                   
Survey Customization | Multilingual Surveys        ❌                     ❌                     ❌                     ✅                   
Survey Customization | Multimedia Support          ❌                     ❌                     ❌                     ✅                   
Survey Insights | Data Exporting                   ❌                     ❌                     ❌                     ✅                   
Survey Insights | Permissions                      ❌                     ❌                     ❌                     ✅                   
Survey Management | Question Types                 ❌                     ❌                     ❌                     ✅                   
Survey Management | Templates                      ❌                     ❌                     ❌                     ✅                   
Training & eLearning | Assessments and Practice    ❌                     ✅                     ✅                     ❌                   
Training & eLearning | Content Creation            ❌                     ✅                     ✅                     ❌                   
Training & eLearning | Content Delivery and Tracking ❌                     ✅                     ✅                     ❌                   
Training & eLearning | Content Libraries           ❌                     ✅                     ✅                     ❌                   
Training & eLearning | Content Storage and Management ❌                     ✅                     ✅                     ❌                   
Training & eLearning | Customer Training           ❌                     ✅                     ❌                     ❌                   
Training & eLearning | Manager Portals             ❌                     ✅                     ✅                     ❌                   

================================================================================
Classroom Messaging
Kriterij                                           SchoolStatus          TalkingPoints         ParentSquare        
--------------------------------------------------------------------------------------------------------------------
Functionality | Analytics                          ✅                     ✅                     ❌                   
Functionality | Mass Messaging                     ✅                     ✅                     ❌                   
Functionality | Multimedia                         ✅                     ✅                     ❌                   
Functionality | Push Notifications                 ✅                     ✅                     ❌                   
Functionality | Student Messaging                  ✅                     ✅                     ❌                   
Integration | Classroom Management                 ✅                     ✅                     ❌                   
Integration | LMS Integration                      ✅                     ✅                     ❌                   
Integration | Message Sync                         ✅                     ✅                     ❌                   

================================================================================
Study Tools
Kriterij                                           Brainscape            Quizlet               Quizizz             
--------------------------------------------------------------------------------------------------------------------
Audience Engagement | Quizzes                      ❌                     ❌                     ✅                   
Engagement Analytics | Dashboards & Reporting      ❌                     ❌                     ✅                   
Engagement Analytics | Live Results                ❌                     ❌                     ✅                   
Event Support | Hybrid/Virtual Events              ❌                     ❌                     ✅                   

================================================================================
Virtual Classroom
Kriterij                                           Zoom Workplace        Speexx              
----------------------------------------------------------------------------------------------
Collaboration | Hand Raising                       ✅                     ✅                   
Collaboration | Participation Controls             ✅                     ✅                   
Collaboration | Screen Sharing                     ✅                     ✅                   
Collaboration | Survey Tools                       ✅                     ✅                   
Collaboration | Whiteboard                         ✅                     ✅                   
Content Sharing | File Sharing                     ✅                     ✅                   
Content Sharing | Session Recording                ✅                     ✅                   
Content Sharing | Video Streaming                  ✅                     ✅                   
Functionality | Live Chat                          ✅                     ✅                   
Functionality | Markup Tools                       ✅                     ✅                   
Functionality | Technical Support                  ✅                     ✅    

'''
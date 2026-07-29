import pandas as pd
from pathlib import Path

files = [
    "data2/features_virtual_classroom3.csv",
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
Virtual Classroom
Kriterij                                           Zoom Workplace        Speexx                Webex Suite           Adobe Connect         powerschool-schoology-learning
----------------------------------------------------------------------------------------------------------------------------------------------------------------
AI - Business Instant Messaging | AI Powered Search ✅                     ❌                     ❌                     ❌                     ❌                   
AI - Business Instant Messaging | Content Generation ✅                     ❌                     ❌                     ❌                     ❌                   
AI - Business Instant Messaging | Smart Notifications ✅                     ❌                     ❌                     ❌                     ❌                   
Access | Browser Extension                         ✅                     ❌                     ✅                     ❌                     ❌                   
Access | Individual Download                       ✅                     ❌                     ✅                     ❌                     ❌                   
Access | Software Pairing                          ✅                     ❌                     ✅                     ❌                     ❌                   
Accessibility - AI Meeting Assistants | Accessibility Guidelines Compliance ❌                     ❌                     ✅                     ❌                     ❌                   
Accessibility - AI Meeting Assistants | Language Translation ❌                     ❌                     ✅                     ❌                     ❌                   
Accessibility - AI Meeting Assistants | Real-Time Transcription ❌                     ❌                     ✅                     ❌                     ❌                   
Accessibility | Keyboard Shortcuts                 ✅                     ❌                     ❌                     ❌                     ❌                   
Accessibility | Screen Reader Compatibility        ✅                     ❌                     ❌                     ❌                     ❌                   
Administration | Administrative Dashboard          ❌                     ✅                     ❌                     ❌                     ❌                   
Administration | Administrative dashboard          ❌                     ✅                     ❌                     ❌                     ❌                   
Administration | Certificates                      ❌                     ✅                     ❌                     ❌                     ❌                   
Administration | Integrations                      ❌                     ✅                     ❌                     ❌                     ❌                   
Administration | Mobile Compatibility              ❌                     ✅                     ❌                     ❌                     ❌                   
Administration | Scheduling                        ❌                     ✅                     ❌                     ❌                     ❌                   
Administration | Team-level monitoring             ❌                     ✅                     ❌                     ❌                     ❌                   
Advanced Features - Cloud PBX | Analytics and Reporting ✅                     ❌                     ❌                     ❌                     ❌                   
Advanced Features - Cloud PBX | Automated attendant ✅                     ❌                     ❌                     ❌                     ❌                   
Advanced Features - Cloud PBX | Security and Compliance ✅                     ❌                     ❌                     ❌                     ❌                   
Advanced Features - Cloud PBX | Support and Reliability ✅                     ❌                     ❌                     ❌                     ❌                   
Advanced Features | Automated Attendants           ✅                     ❌                     ✅                     ❌                     ❌                   
Advanced Features | Hold Music                     ✅                     ❌                     ✅                     ❌                     ❌                   
Advanced Features | VOiP Number                    ❌                     ❌                     ✅                     ❌                     ❌                   
Application Tools | In-Browser Application         ✅                     ❌                     ✅                     ❌                     ❌                   
Application Tools | Password Protection            ✅                     ❌                     ✅                     ❌                     ❌                   
Application Tools | Recording                      ✅                     ❌                     ✅                     ❌                     ❌                   
Attendee Tools | Attendee Live Chat                ❌                     ❌                     ❌                     ✅                     ❌                   
Attendee Tools | Polls and Surveys                 ❌                     ❌                     ❌                     ✅                     ❌                   
Attendee Tools | Registration                      ❌                     ❌                     ❌                     ✅                     ❌                   
Automatic Rules & Configurations | Automatic Updates ✅                     ❌                     ❌                     ❌                     ❌                   
Automatic Rules & Configurations | Buffer Times    ✅                     ❌                     ❌                     ❌                     ❌                   
Automatic Rules & Configurations | Set Working Hours ✅                     ❌                     ❌                     ❌                     ❌                   
Basic Communication - Cloud PBX | Accessibility    ✅                     ❌                     ❌                     ❌                     ❌                   
Basic Communication - Cloud PBX | Call Management  ✅                     ❌                     ❌                     ❌                     ❌                   
Basic Communication - Cloud PBX | Communication Management ✅                     ❌                     ❌                     ❌                     ❌                   
Basic Communication - Cloud PBX | Integrations     ✅                     ❌                     ❌                     ❌                     ❌                   
Basic Communication - Cloud PBX | Mobile Accessibility ✅                     ❌                     ❌                     ❌                     ❌                   
Basic Communication - Cloud PBX | Scalability      ✅                     ❌                     ❌                     ❌                     ❌                   
Basic Communication | Conference Calls             ✅                     ❌                     ✅                     ❌                     ❌                   
Basic Communication | Desk-to-Desk Calls           ✅                     ❌                     ✅                     ❌                     ❌                   
Basic Communication | Instant Messaging            ✅                     ❌                     ✅                     ❌                     ❌                   
Basic Communication | Phone Calls                  ✅                     ❌                     ✅                     ❌                     ❌                   
Basic Communication | Screen Sharing               ✅                     ❌                     ✅                     ❌                     ❌                   
Basic Communication | Video Calls                  ✅                     ❌                     ✅                     ❌                     ❌                   
Branding & Customizatio | Custom Booking Page      ✅                     ❌                     ❌                     ❌                     ❌                   
Branding & Customizatio | Personalized Links       ✅                     ❌                     ❌                     ❌                     ❌                   
Branding & Customizatio | Personalized Web Embed   ✅                     ❌                     ❌                     ❌                     ❌                   
Business Instant Messaging | Audio Conferencing    ✅                     ❌                     ✅                     ❌                     ❌                   
Business Instant Messaging | File Sharing          ✅                     ❌                     ✅                     ❌                     ❌                   
Business Instant Messaging | Integrations          ✅                     ❌                     ✅                     ❌                     ❌                   
Business Instant Messaging | Mobile Application    ✅                     ❌                     ✅                     ❌                     ❌                   
Business Instant Messaging | Notifications         ✅                     ❌                     ✅                     ❌                     ❌                   
Business Instant Messaging | Search                ✅                     ❌                     ✅                     ❌                     ❌                   
Business Instant Messaging | Video Conferencing    ✅                     ❌                     ✅                     ❌                     ❌                   
Business Instant Messaging | Web Application       ✅                     ❌                     ✅                     ❌                     ❌                   
Business Management | Client History               ❌                     ✅                     ❌                     ❌                     ❌                   
Business Management | Surveying                    ❌                     ✅                     ❌                     ❌                     ❌                   
Calendar View | Customizable Viewing               ✅                     ❌                     ❌                     ❌                     ❌                   
Calendar View | Multi-Calendar ViewView full feature definition ✅                     ❌                     ❌                     ❌                     ❌                   
Coaching | Client Plans                            ❌                     ✅                     ❌                     ❌                     ❌                   
Coaching | Goal Tracking                           ❌                     ✅                     ❌                     ❌                     ❌                   
Coaching | Messaging                               ❌                     ✅                     ❌                     ❌                     ❌                   
Coaching | Notekeeping                             ❌                     ✅                     ❌                     ❌                     ❌                   
Coaching | Resource Library                        ❌                     ✅                     ❌                     ❌                     ❌                   
Coaching | Session History                         ❌                     ✅                     ❌                     ❌                     ❌                   
Collaboration Tools | Availability Status          ❌                     ❌                     ✅                     ❌                     ❌                   
Collaboration Tools | Document Sharing             ❌                     ❌                     ✅                     ❌                     ❌                   
Collaboration Tools | Hand Raising                 ✅                     ❌                     ✅                     ✅                     ❌                   
Collaboration Tools | Live Chat                    ✅                     ❌                     ✅                     ✅                     ❌                   
Collaboration Tools | Mobile Application           ❌                     ❌                     ✅                     ❌                     ❌                   
Collaboration Tools | Presentations                ❌                     ❌                     ✅                     ✅                     ❌                   
Collaboration Tools | Screen Sharing               ✅                     ❌                     ✅                     ✅                     ❌                   
Collaboration Tools | Simultaneous Screen Sharing  ❌                     ❌                     ✅                     ❌                     ❌                   
Collaboration Tools | Whiteboarding                ❌                     ❌                     ✅                     ✅                     ❌                   
Collaboration | Board Overview                     ❌                     ❌                     ✅                     ❌                     ❌                   
Collaboration | Hand Raising                       ✅                     ✅                     ✅                     ✅                     ❌                   
Collaboration | Integrated Communications          ❌                     ❌                     ✅                     ❌                     ❌                   
Collaboration | Native Communications              ❌                     ❌                     ✅                     ❌                     ❌                   
Collaboration | Participation Controls             ✅                     ✅                     ✅                     ✅                     ❌                   
Collaboration | Screen Sharing                     ✅                     ✅                     ✅                     ✅                     ❌                   
Collaboration | Survey Tools                       ✅                     ✅                     ✅                     ✅                     ❌                   
Collaboration | Whiteboard                         ✅                     ✅                     ✅                     ✅                     ❌                   
Communication Tools | Commenting                   ✅                     ❌                     ✅                     ❌                     ❌                   
Communication Tools | Voting                       ✅                     ❌                     ✅                     ❌                     ❌                   
Compatibility | Mobile compatibility               ❌                     ✅                     ❌                     ❌                     ❌                   
Compatibility | Single sign-on (SSO)               ❌                     ✅                     ❌                     ❌                     ❌                   
Conferencing Options | Audio Conferencing          ✅                     ❌                     ✅                     ❌                     ❌                   
Conferencing Options | Group Live Chat             ✅                     ❌                     ✅                     ❌                     ❌                   
Conferencing Options | Video Conferencing          ✅                     ❌                     ✅                     ❌                     ❌                   
Content Generation | Content Accuracy              ✅                     ❌                     ❌                     ❌                     ❌                   
Content Generation | Creativity                    ✅                     ❌                     ❌                     ❌                     ❌                   
Content Sharing | File Sharing                     ✅                     ✅                     ✅                     ✅                     ❌                   
Content Sharing | Session Recording                ✅                     ✅                     ✅                     ✅                     ❌                   
Content Sharing | Video Streaming                  ✅                     ✅                     ✅                     ✅                     ❌                   
Coordination Tools | Calendar                      ✅                     ❌                     ❌                     ❌                     ❌                   
Coordination Tools | Contacts                      ✅                     ❌                     ❌                     ❌                     ❌                   
Coordination Tools | Task Management               ✅                     ❌                     ❌                     ❌                     ❌                   
Course Management | Course Access                  ❌                     ✅                     ❌                     ❌                     ❌                   
Courses | Certification practice tests             ❌                     ✅                     ❌                     ❌                     ❌                   
Courses | High-quality content                     ❌                     ✅                     ❌                     ❌                     ❌                   
Courses | In-course assessments                    ❌                     ✅                     ❌                     ❌                     ❌                   
Courses | Personalized recommendations             ❌                     ✅                     ❌                     ❌                     ❌                   
Courses | Projects                                 ❌                     ✅                     ❌                     ❌                     ❌                   
Courses | Video content                            ❌                     ✅                     ❌                     ❌                     ❌                   
Customer Assistance | Help and Support             ❌                     ✅                     ❌                     ❌                     ❌                   
Data | Data Security                               ✅                     ❌                     ❌                     ❌                     ❌                   
Data | Reliability                                 ✅                     ❌                     ❌                     ❌                     ❌                   
Design Tools | Drag-and-Drop                       ✅                     ❌                     ✅                     ❌                     ❌                   
Design Tools | Drawing                             ✅                     ❌                     ✅                     ❌                     ❌                   
Design Tools | Marker Colors                       ✅                     ❌                     ✅                     ❌                     ❌                   
Design Tools | Mind Mapping                        ✅                     ❌                     ✅                     ❌                     ❌                   
Design Tools | Templates                           ✅                     ❌                     ✅                     ❌                     ❌                   
Extensions | CCaaS Option                          ✅                     ❌                     ✅                     ❌                     ❌                   
Extensions | Native VoIP                           ✅                     ❌                     ✅                     ❌                     ❌                   
Extensions | Tenancy Flexibility                   ✅                     ❌                     ✅                     ❌                     ❌                   
Features | Conference Transcripts                  ✅                     ❌                     ✅                     ❌                     ❌                   
Features | File Sharing                            ✅                     ❌                     ✅                     ❌                     ❌                   
Features | Video Conferencing                      ✅                     ❌                     ✅                     ❌                     ❌                   
Features | Voice Conferencing                      ✅                     ❌                     ✅                     ❌                     ❌                   
Features | Voicemail to Email                      ✅                     ❌                     ✅                     ❌                     ❌                   
Features | Voicemail to SMS                        ✅                     ❌                     ✅                     ❌                     ❌                   
Functionality | Live Chat                          ✅                     ✅                     ✅                     ✅                     ❌                   
Functionality | Markup Tools                       ✅                     ✅                     ✅                     ✅                     ❌                   
Functionality | Technical Support                  ✅                     ✅                     ✅                     ✅                     ❌                   
Generative AI - Business Instant Messaging | Text Summarization ✅                     ❌                     ❌                     ❌                     ❌                   
Guest Tools | External Video Conferencing          ❌                     ❌                     ✅                     ❌                     ❌                   
Guest Tools | Guest Links                          ❌                     ❌                     ✅                     ❌                     ❌                   
Guest Tools | Virtual Receptionist                 ❌                     ❌                     ✅                     ❌                     ❌                   
Hardware | Bring Your Own Device                   ❌                     ❌                     ✅                     ❌                     ❌                   
Hardware | Required Hardware                       ❌                     ❌                     ✅                     ❌                     ❌                   
Host Tools | Branding                              ❌                     ❌                     ❌                     ✅                     ❌                   
Host Tools | Recording                             ❌                     ❌                     ❌                     ✅                     ❌                   
Host Tools | Role-based Access                     ❌                     ❌                     ❌                     ✅                     ❌                   
Human Connections | Live Tutoring                  ❌                     ✅                     ❌                     ❌                     ❌                   
Human Connections | Peer Feedback                  ❌                     ✅                     ❌                     ❌                     ❌                   
Inbox Tools | Filters                              ✅                     ❌                     ❌                     ❌                     ❌                   
Inbox Tools | Notifications                        ✅                     ❌                     ❌                     ❌                     ❌                   
Inbox Tools | Reminders                            ✅                     ❌                     ❌                     ❌                     ❌                   
Inbox Tools | Unified Inbox                        ✅                     ❌                     ❌                     ❌                     ❌                   
Integration | Education ERP System                 ❌                     ✅                     ❌                     ❌                     ❌                   
Integration | Import Events                        ✅                     ❌                     ❌                     ❌                     ❌                   
Integration | Learning Management System           ❌                     ✅                     ❌                     ❌                     ❌                   
Integration | Software Integrations                ✅                     ❌                     ❌                     ❌                     ❌                   
Integration | Sync Multiple Calendars              ✅                     ❌                     ❌                     ❌                     ❌                   
Integrations | CMS Integrations                    ✅                     ❌                     ✅                     ❌                     ❌                   
Integrations | Email Integration                   ✅                     ❌                     ❌                     ❌                     ❌                   
Integrations | Google Meet Integration             ✅                     ❌                     ❌                     ❌                     ❌                   
Integrations | MS Teams Integration                ✅                     ❌                     ❌                     ❌                     ❌                   
Integrations | Salesforce Integration              ✅                     ❌                     ❌                     ❌                     ❌                   
Integrations | Sharing                             ✅                     ❌                     ✅                     ❌                     ❌                   
Integrations | Social Media Integration            ❌                     ❌                     ❌                     ✅                     ❌                   
Integrations | Software Integrations               ❌                     ❌                     ❌                     ✅                     ❌                   
Integrations | Zoom Integration                    ✅                     ❌                     ❌                     ❌                     ❌                   
Interaction | Complex Query Handling               ✅                     ❌                     ❌                     ❌                     ❌                   
Interaction | Context Management                   ✅                     ❌                     ❌                     ❌                     ❌                   
Interaction | Customizability                      ✅                     ❌                     ❌                     ❌                     ❌                   
Interaction | Natural Conversation                 ✅                     ❌                     ❌                     ❌                     ❌                   
Interaction | Understanding                        ✅                     ❌                     ❌                     ❌                     ❌                   
Language learning lessons | Gamification           ❌                     ✅                     ❌                     ❌                     ❌                   
Language learning lessons | Multimedia             ❌                     ✅                     ❌                     ❌                     ❌                   
Language learning lessons | Personalized Learning Paths ❌                     ✅                     ❌                     ❌                     ❌                   
Language learning lessons | Self-Paced Lessons     ❌                     ✅                     ❌                     ❌                     ❌                   
Language learning lessons | Speech Recognition     ❌                     ✅                     ❌                     ❌                     ❌                   
Learning | Error Learning                          ✅                     ❌                     ❌                     ❌                     ❌                   
Learning | User Interaction Learning               ✅                     ❌                     ❌                     ❌                     ❌                   
Meeting Automation - AI Meeting Assistants | Action Item Tracking ❌                     ❌                     ✅                     ❌                     ❌                   
Meeting Automation - AI Meeting Assistants | Automated Note-Taking ❌                     ❌                     ✅                     ❌                     ❌                   
Meeting Automation - AI Meeting Assistants | Voice Recognition ❌                     ❌                     ✅                     ❌                     ❌                   
Meeting Coordination | One-Click Join              ✅                     ❌                     ✅                     ✅                     ❌                   
Meeting Coordination | Participant Permissions     ✅                     ❌                     ✅                     ✅                     ❌                   
Meeting Coordination | Recording                   ✅                     ❌                     ✅                     ✅                     ❌                   
Meeting Coordination | Scheduling                  ✅                     ❌                     ✅                     ✅                     ❌                   
Meeting Insights - AI Meeting Assistants | Personalization ❌                     ❌                     ✅                     ❌                     ❌                   
Meeting Insights - AI Meeting Assistants | Sentiment Analysis ❌                     ❌                     ✅                     ❌                     ❌                   
Meeting Insights - AI Meeting Assistants | Smart Summaries ❌                     ❌                     ✅                     ❌                     ❌                   
Meeting Prep - AI Meeting Assistants | Agenda Management ❌                     ❌                     ✅                     ❌                     ❌                   
Meeting Prep - AI Meeting Assistants | Automated Scheduling ❌                     ❌                     ✅                     ❌                     ❌                   
Meeting Prep - AI Meeting Assistants | Virtual Meeting Hosting ❌                     ❌                     ✅                     ❌                     ❌                   
Notifications | Customized Calendar Notifications  ✅                     ❌                     ❌                     ❌                     ❌                   
Notifications | Location-Based Alerts              ✅                     ❌                     ❌                     ❌                     ❌                   
Office Customization | Customized Floor Plans      ❌                     ❌                     ✅                     ❌                     ❌                   
Office Customization | Office Decor                ❌                     ❌                     ✅                     ❌                     ❌                   
Office Customization | Personal Offices            ❌                     ❌                     ✅                     ❌                     ❌                   
Platform Additional Functionality | Asset Management Integration ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Additional Functionality | File Sharing   ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Additional Functionality | Integration    ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Additional Functionality | Network Reporting ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Additional Functionality | Platform Search ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Additional Functionality | Screen Grouping ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Basics | Content Scheduling               ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Basics | Image Editor                     ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Basics | Mail Management                  ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Basics | Multi-User Access                ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Basics | Remotely Content Management      ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Basics | Screen Capture                   ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Basics | Video Capture                    ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Basics | Visitor Check-In                 ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Content | Media Editor                    ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Content | Media Formats                   ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Content | Screen Record                   ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Content | Scrolling Capture               ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Content | Text Extraction                 ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Customization | White Labeling            ❌                     ✅                     ❌                     ❌                     ❌                   
Platform Data | Analytics                          ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Data | Automation                         ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Data | Dashboard                          ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Data | Visitor Logs                       ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Interoperability | Hardware               ✅                     ❌                     ❌                     ❌                     ❌                   
Platform Interoperability | Notifications          ✅                     ❌                     ❌                     ❌                     ❌                   
Post-Event Tools | Attendee Reports                ❌                     ❌                     ❌                     ✅                     ❌                   
Post-Event Tools | Event Analytics                 ❌                     ❌                     ❌                     ✅                     ❌                   
Presenter Tools | Live Preview                     ✅                     ❌                     ✅                     ❌                     ❌                   
Presenter Tools | Notifications Blocker            ✅                     ❌                     ✅                     ❌                     ❌                   
Presenter Tools | Remote Control                   ✅                     ❌                     ✅                     ❌                     ❌                   
Presenter Tools | Switch Presenter                 ✅                     ❌                     ✅                     ❌                     ❌                   
Reporting Analysis | Course Completion             ❌                     ✅                     ❌                     ❌                     ❌                   
Reporting Analysis | Progress Reports              ❌                     ✅                     ❌                     ❌                     ❌                   
Security | Permissions                             ❌                     ❌                     ✅                     ❌                     ❌                   
Security | Single Sign-On (SSO)                    ❌                     ❌                     ✅                     ❌                     ❌                   
Shared Calendar | Calendar Collaboration           ✅                     ❌                     ❌                     ❌                     ❌                   
Shared Calendar | Multiple Calendar Management     ✅                     ❌                     ❌                     ❌                     ❌                   
Software Offering | Desktop App                    ✅                     ❌                     ✅                     ❌                     ❌                   
Software Offering | In-Browser                     ✅                     ❌                     ✅                     ❌                     ❌                   
Software Offering | Mobile App                     ✅                     ❌                     ✅                     ❌                     ❌                   
Software Options | Desktop Application             ✅                     ❌                     ❌                     ❌                     ❌                   
Software Options | Mobile Application              ✅                     ❌                     ❌                     ❌                     ❌                   
Software Type | Browser Application                ✅                     ❌                     ✅                     ✅                     ❌                   
Software Type | Desktop Application                ✅                     ❌                     ✅                     ✅                     ❌                   
Software Type | Mobile                             ✅                     ❌                     ✅                     ✅                     ❌                   
System | API Flexibility                           ✅                     ❌                     ❌                     ❌                     ❌                   
System | Cross-Platform Compatibility              ✅                     ❌                     ❌                     ❌                     ❌                   
System | Software Integration                      ✅                     ❌                     ❌                     ❌                     ❌                   
System | Update Frequency and Utility              ✅                     ❌                     ❌                     ❌                     ❌                   
Visual Tools | Annotations                         ❌                     ❌                     ✅                     ❌                     ❌                   
Visual Tools | Graphing                            ❌                     ❌                     ✅                     ❌                     ❌                   
Visual Tools | Templates                           ❌                     ❌                     ✅                     ❌                     ❌                   
Visual Tools | Whiteboarding                       ❌                     ❌                     ✅                     ❌    

'''
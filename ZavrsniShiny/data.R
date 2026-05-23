# Ovaj fajl ćeš kasnije zamijeniti učitavanjem iz CSV-a
# source("data.R") na vrhu server.R i ui.R

kriteriji <- list(
  "tab_classroom" = list(
    naziv = "Classroom Management",
    kriteriji = c(
      "Remote Computer Monitoring",
      "Student Assignment Distribution",
      "Teacher/Student Screensharing",
      "Interactive Quizzes",
      "Instant Messaging"
    ),
    alati = data.frame(
      naziv     = c("Dyknow Classroom", "ClassDojo", "LanSchool", "Lumio"),
      monitoring = c(97, 86, 87, 89),
      assignment = c(82, 82, 81, 93),
      screenshare= c(91, 85, 88, 94),
      quizzes    = c(81, 74, 78, 92),
      messaging  = c(90, 92, 84, 81)
    )
  ),
  
  "tab_assesment" = list(
    naziv = "Assessment",
    kriteriji = c(
      "Pre-made content",
      "Question variety",
      "Real-time assessment",
      "Gamification",
      "Analytics dashboard"
    ),
    alati = data.frame(
      naziv      = c("Echo360", "iSpring Suite", "Kahoot!", "Mentimeter"),
      premade    = c(92, 83, 88, 82),
      questions  = c(91, 90, 90, 88),
      realtime   = c(93, 86, 96, 95),
      gamification = c(85, 79, 96, 86),
      analytics  = c(78, 77, 91, 86)
    )
  ),
  
  "tab_virtual" = list(
    naziv = "Virtual Classroom",
    kriteriji = c(
      "Video Conferencing",
      "Screen Sharing",
      "Recording",
      "Mobile Compatibility",
      "Integrations"
    ),
    alati = data.frame(
      naziv      = c("Zoom Workplace", "Speexx"),
      video      = c(93, 88),
      screenshare= c(92, 86),
      recording  = c(90, 89),
      mobile     = c(89, 90),
      integrations = c(88, 89)
    )
  )
)
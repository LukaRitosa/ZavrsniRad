
library(shiny)
navbarPage(
  id = "navbar",
  title= "eduTool SMART selektor",
  
  tabPanel(
    "Početna",
  
    fluidRow(
    
      column(8, offset = 2,
      
        tags$br(),
        tags$h2("Biranje nastavnih alata"),
        tags$p("Ova aplikacija pomaže nastvnicima odabrati optimalni 
                digitalni alat za nastavu koristeći SMART metodu 
                operacijskog istraživanja. Odaberi kategoriju alata i
                postavi težine kriterija prema vlastitim potrebama"),
        tags$br(),
        
        tags$h4("Odaberi kategoriju: "),
        tags$br(),
        
        fluidRow(
          column(4,
           actionButton(
               "btn_classroom",
               label = tags$div(
                 tags$h5("Classroom management"),
                 tags$hr(),
                 tags$small("MyClassroom"),tags$br(),
                 tags$small("BlaBlaSchool"),tags$br(),
                 tags$small("OnlineUni"),tags$br(),
                 tags$small("StudentRoom")
               ),
              width = "100%",
              class = "btn btn-outline-primary text-start w-100 p-3"
            )
          ),
          
          column(4,
            actionButton(
             "btn_assesment",
             label = tags$div(
               tags$h5("Assesment"),
               tags$hr(),
               tags$small("Kahoot"),tags$br(),
               tags$small("Quizzler"),tags$br(),
               tags$small("eLearner"),tags$br(),
               tags$small("Mentimeter")
             ),
             width = "100%",
             class = "btn btn-outline-primary text-start w-100 p-3"
            )
          ),
          
          column(4,
            actionButton(
             "btn_virtual",
             label = tags$div(
               tags$h5("Virtual Classroom"),
               tags$hr(),
               tags$small("Zoom"),tags$br(),
               tags$small("Google Meet")
             ),
             width = "100%",
             class = "btn btn-outline-primary text-start w-100 p-3"
            )
          )
        )
      )
    )
  ),
  
  tabPanel("Classroom management", value = "tab_classroom",
    fluidRow(
      column(8, offset = 2,
        tags$br(),
        tags$h3("Classroom management"),
        tags$p("Bla bla classroom")
      )
    )
  ),
  
  tabPanel("Assesment", value = "tab_assesment",
    fluidRow(
      column(8, offset = 2,
        tags$br(),
        tags$h3("Assesment"),
        tags$p("Bla bla assesment")
      )
    )
  ),
  
  tabPanel("Virtual Classroom", value = "tab_virtual",
    fluidRow(
      column(8, offset = 2,
        tags$br(),
        tags$h3("Virtual Classroom"),
        tags$p("Bla bla Virtual")
      )
    )
  )
  
)
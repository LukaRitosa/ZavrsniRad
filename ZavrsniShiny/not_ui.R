library(shiny)
library(sortable)
source("data.R")

do.call(navbarPage, c(
  list(
    id = "navbar",
    title= "eduTool SMART selektor"
  ),
  
  list(tabPanel(
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
               lapply(names(kriteriji), function(tab_id){
                 btn_name <- paste0("btn_", gsub("tab_", "", tab_id), "_ui")
                 print(paste("UI traži:", btn_name))
                 column(4, uiOutput(btn_name))
               })
             )
      )
    )
  )),
  
  lapply(names(kriteriji), function(tab_id){
    kat <- kriteriji[[tab_id]]
    tabPanel(
      kat$naziv,
      value= tab_id,
      fluidRow(
        column(8, offset = 2,
               tags$br(),
               tags$h3(kat$naziv),
               
               
               uiOutput(paste0("odabir_ui_", tab_id)),
               
               uiOutput(paste0("ranking_ui_", tab_id)),
               
               
               
        )
      )
    )
  })
  
))
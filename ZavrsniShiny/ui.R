library(shiny)
library(sortable)
source("data.R")

library(bslib)

do.call(navbarPage, c(
  list(
    id = "navbar",
    title= "eduTool SMART selektor",
    theme = bs_theme(
      version = 5,
      bootswatch = "flatly"
    )
  ),
  
  list(tabPanel(
    "Početna",
    
    fluidRow(
      
      column(8, offset = 2,
             
        tags$br(),
        tags$h2("Biranje nastavnih alata"),
        tags$p("Ova aplikacija pomaže nastvnicima odabrati optimalni 
          digitalni alat za nastavu koristeći SMART metodu 
          operacijskih istraživanja. Odeberite kategoriju alata
          koja Vam je potrebna, izaberite releventne funkcionalnosti, 
          rangirajte funkcionalnosti te dodijelite intenzitet razlika između funkcionalnosti"),
        
        tags$br(),
        
        tags$h4("Odaberite kategoriju: "),
        tags$br(),
        
        fluidRow(
         lapply(names(kriteriji), function(tab_id){
           btn_name <- paste0("btn_", gsub("tab_", "", tab_id), "_ui")
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
          
          uiOutput(paste0("step_ui_", tab_id)),
          
          uiOutput(paste0("odabir_ui_", tab_id)),
          
          uiOutput(paste0("ranking_ui_", tab_id)),

          uiOutput(paste0("weight_ui_", tab_id)),
          
          uiOutput(paste0("rezultat_", tab_id))
        )
      )
    )
  })
  
))
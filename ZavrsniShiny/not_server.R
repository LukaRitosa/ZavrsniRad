library(shiny)
library(sortable)
source("data.R")

function(input, output, session) {
  
  lapply(names(kriteriji), function(tab_id){
    btn_output_id <- paste0("btn_", gsub("tab_", "", tab_id), "_ui")
    print(paste("Server renderira:", btn_output_id))
    btn_input_id <- paste0("btn_", gsub("tab_", "", tab_id))
    
    show_ranking <- reactiveVal(FALSE)
    
    output[[btn_output_id]] <- renderUI({
      kat <- kriteriji[[tab_id]]
      actionButton(
        inputId = btn_input_id,
        label = tags$div(
          tags$h5(kat$naziv),
          tags$hr(),
          tagList(lapply(kat$alati$naziv, function(a) {
            tagList(tags$small(a), tags$br())
          }))
        ),
        width = "100%",
        class = "btn btn-outline-primary text-start w-100 p-3"
      )
    })
    
    output[[paste0("odabir_ui_", tab_id)]] <- renderUI({
      
      if(!show_ranking()) {
        
        tagList(
          
          tags$p("Odaberi kriterije za analizu:"),
          
          checkboxGroupInput(
            inputId = paste0("odabir_", tab_id),
            label = NULL,
            choices = kriteriji[[tab_id]]$kriteriji,
            selected = kriteriji[[tab_id]]$kriteriji
          ),
          
          actionButton(
            paste0("btn_potvrdi_", tab_id),
            "Potvrdi kriterije",
            class = "btn btn-secondary"
          )
        )
      }
    })
    
    output[[paste0("ranking_ui_", tab_id)]] <- renderUI({
      if(show_ranking()) {
        tagList(
          tags$p("Povuci i poredaj kriterije (1 = najvažnije):"),
          rank_list(
            text     = "",
            labels   = input[[paste0("odabir_", tab_id)]],
            input_id = paste0("rang_", tab_id)
          ),
          tags$br(),
          actionButton(
            paste0("btn_izracun_", tab_id),
            "Izračunaj",
            class = "btn btn-primary"
          ),
          tags$br(),
          actionButton(
            paste0("btn_natrag_", tab_id),
            "Vrati se na odabir",
            class = "btn btn-warning btn-sm"
          ),
          tags$br(), tags$br(),
          uiOutput(paste0("rezultat_", tab_id))
        )
      }
    })
    
    observeEvent(input[[paste0("btn_potvrdi_", tab_id)]], {
      
      req(input[[paste0("odabir_", tab_id)]])
      req(length(input[[paste0("odabir_", tab_id)]]) > 0)
      
      show_ranking(TRUE)
    })
    
    observeEvent(input[[paste0("btn_natrag_", tab_id)]], {
      
      show_ranking(FALSE)
    })
    
    
  })
  
  
  
  lapply(names(kriteriji), function(tab_id){
    
    btn_input_id <- paste0("btn_", gsub("tab_", "", tab_id))
    
    observeEvent(input[[btn_input_id]], {
      updateNavbarPage(session, inputId = "navbar",selected = tab_id)
    })
    
  })
  
  smart_izracun <- function(poredak, kat) {
    df <- kat$alati
    n  <- length(poredak)
    
    tezine_raw  <- (n - seq_along(poredak) + 1)
    tezine_norm <- tezine_raw / sum(tezine_raw)
    names(tezine_norm) <- poredak
    

    krit_to_col <- setNames(names(df)[-1], kat$kriteriji)
    cols_odabrani <- krit_to_col[poredak]
    
    df$score <- round(
      rowSums(sweep(df[, cols_odabrani], 2, tezine_norm, "*")),
      1
    )
    
    df <- df[order(-df$score), ]
    df$rang <- 1:nrow(df)
    df
  }
  
  rez_ui <- function(df){
    tagList(
      tags$div(
        class= "alert alert-success",
        tags$h5("Preporučeni alat:"),
        tags$h4(df$naziv[1]),
        tags$p(paste0("SMART skor: ", df$score[1]))
      ),
      tags$h6("Rang lista:"),
      tags$table(
        class = "table table-striped",
        tags$thead(tags$tr(
          tags$th("Rang"), tags$th("Alat"), tags$th("Skor")
        )),
        tags$tbody(
          lapply(seq_len(nrow(df)), function(i){
            tags$tr(
              tags$td(df$rang[i]),
              tags$td(df$naziv[i]),
              tags$td(df$score[i])
            )
          })
        )
      )
    )
  }
  
  lapply(names(kriteriji), function(tab_id){
    observeEvent(input[[paste0("btn_izracun_", tab_id)]],{
      df <- smart_izracun(input[[paste0("rang_", tab_id)]], kriteriji[[tab_id]])
      output[[paste0("rezultat_", tab_id)]] <- renderUI(rez_ui(df))
    })
  })
  
  
  
}

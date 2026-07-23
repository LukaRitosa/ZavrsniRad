library(shiny)
library(sortable)
source("data.R")

function(input, output, session) {
  
  step <- lapply(names(kriteriji), function(x) reactiveVal("select"))
  names(step) <- names(kriteriji)
  
  lapply(names(kriteriji), function(tab_id){
    btn_output_id <- paste0("btn_", gsub("tab_", "", tab_id), "_ui")
    btn_input_id <- paste0("btn_", gsub("tab_", "", tab_id))
    
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
      
      if(step[[tab_id]]() == "select") {
        
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
      if(step[[tab_id]]() == "ranking") {
        tagList(
          tags$p("Povuci i poredaj kriterije (1 = najvažnije):"),
          rank_list(
            text     = "",
            labels   = input[[paste0("odabir_", tab_id)]],
            input_id = paste0("rang_", tab_id)
          ),
          tags$br(),
          actionButton(
            paste0("btn_na_weight_", tab_id),
            "Dalje",
            class = "btn btn-primary"
          ),
          tags$br(),
          actionButton(
            paste0("btn_natrag_", tab_id),
            "Vrati se na odabir",
            class = "btn btn-warning btn-sm"
          ),
          tags$br(), tags$br()
        )
      }
    })
    
    output[[paste0("weight_ui_", tab_id)]] <- renderUI({
      if(step[[tab_id]]() == "weight"){
        poredak <- input[[paste0("rang_", tab_id)]]
        n <- length(poredak)
        
        pitanja <- lapply(1:(n-1), function(i){
          tagList(
            tags$p(
              tags$strong(
                paste0("Koliko puta vam je '", poredak[i], "' važniji od '", poredak[i+1],"'?")
              )
            ),
            selectInput(
              inputId = paste0("weight_", tab_id, "_", i),
              label = NULL,
              choices = 2 : 10,
              selected = 2,
              width = "100px"
            ),
            tags$hr()
          )
        })
        tagList(
          pitanja,
          actionButton(
            paste0("btn_izracun_", tab_id),
            "Izračunaj",
            class = "btn btn-primary"
          ),
          actionButton(
            paste0("btn_natrag_weight_", tab_id),
            "Natrag na rangiranje",
            class = "btn btn-warning btn-sm ms-2"
          ),
          tags$br(), tags$br()
        )
      }
    })
    
    output[[paste0("rezultat_", tab_id)]] <- renderUI({
      if(step[[tab_id]]() == "result"){
        uiOutput(paste0("rezultat_sadrzaj_", tab_id))
      }
    })
    
    observeEvent(input[[paste0("btn_potvrdi_", tab_id)]], {
      
      req(input[[paste0("odabir_", tab_id)]])
      req(length(input[[paste0("odabir_", tab_id)]]) > 0)
      
      step[[tab_id]]("ranking")
    })
    
    observeEvent(input[[paste0("btn_natrag_", tab_id)]], {
      
      step[[tab_id]]("select")
    })
    
    observeEvent(input[[paste0("btn_natrag_weight_", tab_id)]], {
      step[[tab_id]]("ranking")
    })
    
    
    observeEvent(input[[paste0("btn_na_weight_", tab_id)]], {
      step[[tab_id]]("weight")
    })
    
    observeEvent(input[[paste0("btn_natrag_rezultat_", tab_id)]],{
      step[[tab_id]]("weight")
    })
  })
  
  
  
  lapply(names(kriteriji), function(tab_id){
    
    btn_input_id <- paste0("btn_", gsub("tab_", "", tab_id))
    
    observeEvent(input[[btn_input_id]], {
      updateNavbarPage(session, inputId = "navbar",selected = tab_id)
    })
    
  })
  
  smart_izracun <- function(poredak, kat, weight_omjeri) {
    df <- kat$alati
    n  <- length(poredak)
    
    tezine <- numeric(n)
    tezine[n] <- 10
    
    if(n>1){
      for(i in (n-1) : 1){
        tezine[i] <- tezine[i + 1] * weight_omjeri[i]
      }
    }
    
    tezine_norm <- tezine / sum(tezine)
    names(tezine_norm) <- poredak
    
    feature_cols <- setdiff(
      names(df), c("naziv", "slug", "category","rating")
    )

    krit_to_col <- setNames(feature_cols, kat$kriteriji)
    cols_odabrani <- krit_to_col[poredak]
    
    df$score <- round(
      rowSums(sweep(df[, cols_odabrani], 2, tezine_norm, "*")),
      1
    )
    
    df <- df[order(-df$score), ]
    df$rang <- 1:nrow(df)
    df
  }
  
  rez_ui <- function(df, tab_id){
    g2_link <- paste0("https://www.g2.com/products/", df$slug[1], "/reviews")
    
    tagList(
      tags$div(
        class= "alert alert-success",
        tags$h5("Preporučeni alat:"),
        tags$h4(df$naziv[1]),
        tags$p(paste0("SMART skor: ", df$score[1])),
        
        tags$p(strong("Ocjena na G2: "), df$rating[1], " / 5"),
        
        tags$a("G2 recenzije", href = g2_link, target = "_blank", class = "btn btn-primary"
        )
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
      ),
      
      tags$br(),
      
      actionButton(
        paste0("btn_natrag_rezultat_", tab_id),
        "Natrag na težine",
        class = "btn btn-warning"
      )
    )
  }
  
  lapply(names(kriteriji), function(tab_id){
    observeEvent(input[[paste0("btn_izracun_", tab_id)]],{
      
      poredak <- input[[paste0("rang_", tab_id)]]
      n <- length(poredak)
      
      weight_omjeri <- if(n > 1){
        sapply(1:(n-1), function(i){
          val <- as.numeric(input[[paste0("weight_", tab_id, "_", i)]])
          if(is.null(val) || val < 1) 1 else val
        })
      } else{
        numeric(0)
      }
        
      df <- smart_izracun(poredak, kriteriji[[tab_id]], weight_omjeri)
      
      output[[paste0("rezultat_sadrzaj_", tab_id)]] <- renderUI(rez_ui(df, tab_id))
  
      step[[tab_id]]("result")
    })
  })
  
  
  
}

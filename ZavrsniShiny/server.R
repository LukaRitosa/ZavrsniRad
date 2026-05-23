library(shiny)

function(input, output, session) {

  observeEvent(input$btn_classroom, {
    updateNavbarPage(session, inputId = "navbar", selected = "tab_classroom")
  })
  
  observeEvent(input$btn_assesment, {
    updateNavbarPage(session, inputId = "navbar", selected = "tab_assesment")
  })
  
  observeEvent(input$btn_virtual, {
    updateNavbarPage(session, inputId = "navbar", selected = "tab_virtual")
  })

}

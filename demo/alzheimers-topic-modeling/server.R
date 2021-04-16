
library(shiny)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
  
    model <- reactive(input$model)
    topic <- reactive(input$topic)

    output$docImg <- renderImage({
      docpath <- paste("plots/documents-plots/",model(),"/",topic(),".png",sep="")
      list(src=docpath,width=600,height=600)
    },deleteFile = FALSE)
    
    output$wcImg <- renderImage({
      docpath <- paste("plots/wordcloud-plots/",model(),"/",topic(),".png",sep="")
      list(src=docpath,width=360,height=360)
    },deleteFile = FALSE)
    
    output$allTopics <- renderImage({
      docpath <- paste("plots/topic/",model(),".png",sep="")
      list(src=docpath,width=480,height=450)
    },deleteFile = FALSE)
    
    output$topicMeta <- renderImage({
      docpath <- paste("plots/topic-meta/",model(),"/",topic(),".png",sep="")
      list(src=docpath,width=360,height=360)
    },deleteFile = FALSE)
    
    output$covariate <- renderImage({
      docpath <- paste("plots/topic-covariate/",model(),".png",sep="")
      list(src=docpath,width=480, heiht="auto")
    },deleteFile = FALSE)
  
})


library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  h1("Alzheimer's Forums Topic Modeling"),
  
  hr(),
  
  # fluid row for inputs
  fluidRow(align="center",
    column(5,
      selectInput("model", "Choose a model:",
                  choices = list("stm-20","stm-30","selected-20","selected-30"))
    ),
    column(6,
      sliderInput("topic",
                   "Topic number: ",
                   min = 1,
                   max = 30,
                   value = 1)
      )
  ),

  # output images
    hr(),
  fluidRow(
    column(4,
      h4("All Topics"),
      br(),
      imageOutput(outputId="allTopics"),
      br(),
      imageOutput(outputId="covariate")),
    column(5,
      h4("Representative documents for this topic:"),
      br(),
      imageOutput(outputId="docImg")),
    column(3,
      h4("Wordcloud for topic words: "),
      imageOutput(outputId="wcImg"),
      h4("Topic-Forum Relationship:"),
      imageOutput(outputId="topicMeta"))


  )

  
))

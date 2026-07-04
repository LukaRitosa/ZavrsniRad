library(readr)

classroom <- read_csv(
  "data/features_classroom_management2.csv",
  show_col_types = FALSE
)

assessment <- read_csv(
  "data/features_assessment2.csv",
  show_col_types = FALSE
)

virtual <- read_csv(
  "data/features_virtual_classroom2.csv",
  show_col_types = FALSE
)


napravi_kategoriju <- function(df){
  osnovni <- c(
    "name",
    "slug",
    "category",
    "rating"
  )
  
  kriteriji <- setdiff(
    names(df),
    osnovni
  )
  
  alati <- df
  
  names(alati)[names(alati)=="name"] <- "naziv"
  
  list(
    naziv= unique(df$category),
    
    kriteriji = kriteriji,
    
    alati=alati,
    
    meta= df[, c(
      "name",
      "slug",
      "category",
      "rating"
    )]
  )
}

kriteriji <- list(
  tab_classroom = napravi_kategoriju(classroom),
  
  tab_assessment= napravi_kategoriju(assessment),
  
  tab_virtual= napravi_kategoriju(virtual)
)


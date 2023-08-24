# This code reads the CSV of patient data, and saves a histogram of ages to a new file.
# https://docs.opensafely.org/getting-started/#add-a-chart

library('tidyverse')

df_input <- read_csv(
  here::here("output", "input.csv.gz"),
  col_types = cols(patient_id = col_integer(),age = col_double())
)

plot_age <- ggplot(data=df_input, aes(df_input$age)) + geom_histogram()

ggsave(
  plot= plot_age,
  filename="descriptive.png", path=here::here("output"),
)

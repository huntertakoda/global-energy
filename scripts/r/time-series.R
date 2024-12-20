library(tidyverse)
library(forecast)
library(lubridate)

# loading

file_path <- "C:/data/energy_sustainability_dataset.csv"
energy_data <- read_csv(file_path)

# prepare time-series data for co2 emissions

co2_time_series <- energy_data %>% 
  group_by(Year) %>% 
  summarise(total_co2_emissions = sum(CO2_Emissions, na.rm = TRUE)) %>% 
  arrange(Year)

co2_ts <- ts(co2_time_series$total_co2_emissions, start = min(co2_time_series$Year), frequency = 1)

# visualize the time-series data

autoplot(co2_ts) +
  labs(
    title = "total co2 emissions over time",
    x = "year",
    y = "co2 emissions"
  ) +
  theme_minimal()

# fit an arima model

arima_model <- auto.arima(co2_ts)
print("arima model summary:")
print(summary(arima_model))

# forecast future co2 emissions for the next 5 years

forecasted_co2 <- forecast(arima_model, h = 5)

# visualize the forecast

autoplot(forecasted_co2) +
  labs(
    title = "forecasted co2 emissions for the next 5 years",
    x = "year",
    y = "co2 emissions"
  ) +
  theme_minimal()

# save the forecasted values to a file

forecasted_data <- data.frame(
  year = seq(max(co2_time_series$Year) + 1, max(co2_time_series$Year) + 5),
  forecasted_co2_emissions = as.numeric(forecasted_co2$mean)
)
write.csv(forecasted_data, "C:/data/forecasted_co2_emissions.csv", row.names = FALSE)

# script execution complete

print("time-series analysis completed successfully.")

library(tidyverse)

# loading

file_path <- "C:/data/energy_sustainability_dataset.csv"
energy_data <- read_csv(file_path)

# summarizing

summary_stats <- energy_data %>% 
  summarise(
    avg_energy_consumption = mean(Energy_Consumption, na.rm = TRUE),
    avg_renewable_percentage = mean(Renewable_Percentage, na.rm = TRUE),
    avg_co2_emissions = mean(CO2_Emissions, na.rm = TRUE),
    total_population = sum(Population, na.rm = TRUE)
  )

print("summary statistics:")
print(summary_stats)

# correlation matrix

correlation_matrix <- energy_data %>% 
  select(Energy_Consumption, Renewable_Percentage, Fossil_Percentage, 
         CO2_Emissions, GDP, Population) %>% 
  cor(use = "complete.obs")

print("correlation matrix:")
print(correlation_matrix)

# energy consumption vs renewable percentage

ggplot(energy_data, aes(x = Renewable_Percentage, y = Energy_Consumption)) +
  geom_point(alpha = 0.6, color = "blue") +
  labs(
    title = "energy consumption vs renewable percentage",
    x = "renewable percentage",
    y = "energy consumption"
  ) +
  theme_minimal()

# save correlation matrix to a file

write.csv(correlation_matrix, "C:/data/correlation_matrix.csv")

# execution complete

print("statistical analysis completed successfully.")

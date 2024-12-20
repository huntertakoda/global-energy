library(tidyverse)
library(car) 
library(lmtest) 
library(mgcv) 

# loading

file_path <- "C:/data/energy_sustainability_dataset.csv"
energy_data <- read_csv(file_path)

# perform multiple linear regression for co2 emissions

regression_model <- lm(CO2_Emissions ~ Energy_Consumption + Renewable_Percentage + GDP + Population, data = energy_data)

print("regression model summary:")
print(summary(regression_model))

# check for multicollinearity using vif

print("variance inflation factor (vif):")
vif_values <- vif(regression_model)
print(vif_values)

# perform residual diagnostics for the regression model

print("breusch-pagan test for heteroscedasticity:")
bptest_result <- bptest(regression_model)
print(bptest_result)

# fit a generalized additive model (gam) for co2 emissions

gam_model <- gam(CO2_Emissions ~ s(Energy_Consumption) + s(Renewable_Percentage) + s(GDP) + s(Population), data = energy_data)

print("gam model summary:")
print(summary(gam_model))

# visualize gam smooth terms

par(mfrow = c(2, 2)) # set plotting area for gam terms
plot(gam_model, se = TRUE, col = "blue")

# save model coefficients and diagnostics to files

coefficients <- data.frame(
  variable = names(coef(regression_model)),
  coefficient = coef(regression_model)
)
write.csv(coefficients, "C:/data/regression_coefficients.csv", row.names = FALSE)

gam_summaries <- summary(gam_model)$s.table
write.csv(gam_summaries, "C:/data/gam_smooth_summaries.csv", row.names = TRUE)

# script execution complete

print("advanced statistical analysis completed successfully.")

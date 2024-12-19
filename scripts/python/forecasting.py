import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# load the enhanced dataset

file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data = pd.read_csv(file_path)

# prepare time-series data for forecasting

print("\nPreparing time-series data...")
data['Year'] = data['Year'].astype(int)  # Ensure Year is an integer
time_series_data = data.groupby('Year')['CO2_Emissions'].mean()

# fit an ARIMA model

print("\nFitting ARIMA model...")
model = ARIMA(time_series_data, order=(1, 1, 1))
arima_result = model.fit()

# make future predictions (next 5 years)

print("\nMaking future predictions...")
forecast_steps = 5
forecast_index = range(time_series_data.index[-1] + 1, time_series_data.index[-1] + 1 + forecast_steps)
forecast = arima_result.forecast(steps=forecast_steps)

# display forecasted values

print("\nForecasted CO2 Emissions for the next 5 years:")
for year, value in zip(forecast_index, forecast):
    print(f"Year {year}: {value:.2f}")

# plot historical data

print("\nPlotting historical CO2 emissions...")
plt.figure(figsize=(10, 6))
plt.plot(time_series_data.index, time_series_data.values, label="Historical CO2 Emissions")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions")
plt.title("Historical CO2 Emissions")
plt.legend()
plt.show()

# plot forecasted data

print("\nPlotting forecast...")
plt.figure(figsize=(10, 6))
plt.plot(time_series_data.index, time_series_data.values, label="Historical CO2 Emissions")
plt.plot(forecast_index, forecast, label="Forecast", color="orange")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions")
plt.title("CO2 Emissions Forecast with Historical Data")
plt.legend()
plt.show()

# print success message

print("Forecasting completed successfully.")

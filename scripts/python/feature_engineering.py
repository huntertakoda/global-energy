import pandas as pd
import numpy as np

# load the preprocessed dataset

file_path = "C:/data/preprocessed_energy_dataset.csv"
data = pd.read_csv(file_path)

# create a new feature: energy consumption per capita

print("\nCreating energy consumption per capita...")
data['Energy_Consumption_Per_Capita'] = data['Energy_Consumption'] / data['Population']

# create a new feature: emissions intensity (CO2 emissions per GDP)

print("\nCreating emissions intensity...")
data['Emissions_Intensity'] = data['CO2_Emissions'] / data['GDP']

# create a categorical feature for high renewable energy adoption

print("\nCategorizing renewable energy adoption...")
data['High_Renewable_Adoption'] = np.where(data['Renewable_Percentage'] > 30, 1, 0)

# create a new feature: fossil fuel to renewable ratio

print("\nCreating fossil fuel to renewable ratio...")
data['Fossil_to_Renewable_Ratio'] = data['Fossil_Percentage'] / (data['Renewable_Percentage'] + 1e-6)

# drop unnecessary columns (if any)

print("\nDropping unnecessary columns...")
data.drop(columns=['Nuclear_Energy'], inplace=True)

# save the enhanced dataset with new features

enhanced_file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data.to_csv(enhanced_file_path, index=False)

# print success message

print("Feature engineering completed successfully. Enhanced dataset saved to:", enhanced_file_path)

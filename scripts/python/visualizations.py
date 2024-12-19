import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the enhanced dataset

file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data = pd.read_csv(file_path)

# plot energy consumption distribution

print("\nPlotting energy consumption distribution...")
plt.figure(figsize=(10, 6))
sns.histplot(data['Energy_Consumption'], bins=30, kde=True, color="skyblue")
plt.title("Distribution of Energy Consumption")
plt.xlabel("Energy Consumption (MWh)")
plt.ylabel("Frequency")
plt.show()

# plot renewable energy percentage vs fossil fuel percentage

print("\nPlotting renewable vs fossil fuel percentage...")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['Renewable_Percentage'], y=data['Fossil_Percentage'], hue=data['High_Renewable_Adoption'])
plt.title("Renewable Percentage vs Fossil Fuel Percentage")
plt.xlabel("Renewable Percentage")
plt.ylabel("Fossil Percentage")
plt.legend(title="High Renewable Adoption")
plt.show()

# plot CO2 emissions over years

print("\nPlotting CO2 emissions over years...")
avg_emissions_per_year = data.groupby('Year')['CO2_Emissions'].mean()
plt.figure(figsize=(10, 6))
plt.plot(avg_emissions_per_year.index, avg_emissions_per_year.values, marker='o', color="green")
plt.title("Average CO2 Emissions Over Years")
plt.xlabel("Year")
plt.ylabel("Average CO2 Emissions")
plt.grid(True)
plt.show()

# plot regional renewable energy adoption

print("\nPlotting regional renewable energy adoption...")
region_cols = [col for col in data.columns if col.startswith('Region_')]
regional_data = data[region_cols + ['Renewable_Percentage']].melt(
    id_vars='Renewable_Percentage', var_name='Region', value_name='Presence')
regional_avg = regional_data.groupby('Region')['Renewable_Percentage'].mean()
plt.figure(figsize=(10, 6))
regional_avg.sort_values().plot(kind='bar', color="orange")
plt.title("Average Renewable Energy Percentage by Region")
plt.xlabel("Region")
plt.ylabel("Average Renewable Percentage")
plt.show()

# print success message

print("Visualizations completed successfully.")

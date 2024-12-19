import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the preprocessed dataset

file_path = "C:/data/preprocessed_energy_dataset.csv"
data = pd.read_csv(file_path)

# display basic dataset information

print("Dataset Info:")
print(data.info())

# display summary statistics for numerical columns

print("\nSummary Statistics:")
print(data.describe())

# generate correlation matrix and heatmap (numerical columns only)

print("\nGenerating correlation heatmap...")
numerical_data = data.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
correlation_matrix = numerical_data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# plot distribution of energy consumption

print("\nPlotting energy consumption distribution...")
plt.figure(figsize=(8, 6))
sns.histplot(data['Energy_Consumption'], bins=30, kde=True)
plt.title("Energy Consumption Distribution")
plt.xlabel("Energy Consumption (MWh)")
plt.ylabel("Frequency")
plt.show()

# plot renewable percentage by region

print("\nPlotting renewable percentage by region...")
region_cols = [col for col in data.columns if col.startswith('Region_')]
renewable_data = data[['Renewable_Percentage'] + region_cols].melt(
    id_vars=['Renewable_Percentage'], var_name='Region', value_name='Presence')
region_means = renewable_data.groupby('Region')['Renewable_Percentage'].mean()
plt.figure(figsize=(10, 6))
region_means.plot(kind='bar', color='skyblue')
plt.title("Average Renewable Percentage by Region")
plt.ylabel("Average Renewable Percentage")
plt.xticks(rotation=45)
plt.show()

# print success message

print("EDA completed successfully.")

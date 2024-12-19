import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# load the enhanced dataset

file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data = pd.read_csv(file_path)

# pairplot for key numerical features

print("\nGenerating pairplot for key features...")
key_features = [
    'Energy_Consumption', 'Renewable_Percentage', 'Fossil_Percentage',
    'CO2_Emissions', 'Population', 'GDP', 'Urbanization_Rate'
]
sns.pairplot(data[key_features], diag_kind="kde", plot_kws={"alpha": 0.5})
plt.suptitle("Pairplot of Key Numerical Features", y=1.02)
plt.show()

# heatmap for feature correlation with annotations

print("\nGenerating advanced correlation heatmap...")
plt.figure(figsize=(12, 8))
correlation_matrix = data[key_features].corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# boxplot of energy intensity by high renewable adoption

print("\nGenerating boxplot for energy intensity by renewable adoption...")
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['High_Renewable_Adoption'], y=data['Energy_Intensity'], palette="Set2")
plt.title("Energy Intensity by High Renewable Adoption")
plt.xlabel("High Renewable Adoption")
plt.ylabel("Energy Intensity")
plt.show()

# jointplot for emissions intensity vs urbanization rate

print("\nGenerating jointplot for emissions intensity and urbanization rate...")
sns.jointplot(
    x=data['Urbanization_Rate'], y=data['Emissions_Intensity'], kind="reg", height=8, color="purple"
)
plt.suptitle("Emissions Intensity vs Urbanization Rate", y=1.02)
plt.show()

# violin plot of CO2 emissions by region

print("\nGenerating violin plot for CO2 emissions by region...")
region_cols = [col for col in data.columns if col.startswith('Region_')]
data['Region'] = data[region_cols].idxmax(axis=1).str.replace('Region_', '')  # Derive region from one-hot encoding
plt.figure(figsize=(12, 6))
sns.violinplot(x='Region', y='CO2_Emissions', data=data, palette="muted")
plt.title("CO2 Emissions by Region")
plt.xlabel("Region")
plt.ylabel("CO2 Emissions")
plt.show()

# print success message

print("Advanced visualizations completed successfully.")

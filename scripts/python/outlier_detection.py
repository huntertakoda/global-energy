import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# load the enhanced dataset

file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data = pd.read_csv(file_path)

# detect outliers in energy consumption using isolation forest

print("\nDetecting outliers in energy consumption...")
isolation_forest = IsolationForest(contamination=0.05, random_state=42)
data['Outlier'] = isolation_forest.fit_predict(data[['Energy_Consumption']])

# visualize outliers

print("\nVisualizing outliers...")
plt.figure(figsize=(10, 6))
plt.scatter(data['Energy_Consumption'], data['CO2_Emissions'], c=data['Outlier'], cmap="coolwarm", alpha=0.7)
plt.xlabel("Energy Consumption")
plt.ylabel("CO2 Emissions")
plt.title("Outliers in Energy Consumption")
plt.colorbar(label="Outlier")
plt.show()

# save the dataset with outliers marked

outlier_file_path = "C:/data/outlier_detected_energy_dataset.csv"
data.to_csv(outlier_file_path, index=False)

# print success message

print("Outlier detection completed successfully. Dataset saved to:", outlier_file_path)

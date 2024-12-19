# import necessary libraries

import pandas as pd
import numpy as np

# load the enhanced dataset

file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data = pd.read_csv(file_path)

# inspect the target variable distribution

print("\nInspecting target variable distribution...")
print(data['High_Renewable_Adoption'].value_counts())

# adjust the threshold for high renewable adoption if needed

if len(data['High_Renewable_Adoption'].unique()) < 2:
    print("\nAdjusting threshold for High Renewable Adoption...")
    data['High_Renewable_Adoption'] = np.where(data['Renewable_Percentage'] > 25, 1, 0)
    print("New target variable distribution:")
    print(data['High_Renewable_Adoption'].value_counts())

# save the adjusted dataset

adjusted_file_path = "C:/data/adjusted_feature_enhanced_energy_dataset.csv"
data.to_csv(adjusted_file_path, index=False)

print("Adjusted dataset saved to:", adjusted_file_path)

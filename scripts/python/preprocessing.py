import pandas as pd
import numpy as np

# load the dataset

file_path = "C:/data/synthetic_energy_sustainability_dataset.csv"
data = pd.read_csv(file_path)

# handle missing values by filling with mean for numerical columns

data.fillna(data.mean(numeric_only=True), inplace=True)

# normalize numerical columns for better analysis

numeric_cols = data.select_dtypes(include=np.number).columns
data[numeric_cols] = (data[numeric_cols] - data[numeric_cols].mean()) / data[numeric_cols].std()

# standardize categorical features (region) using one-hot encoding

data = pd.get_dummies(data, columns=['Region'], drop_first=True)

# save the cleaned and preprocessed dataset

preprocessed_file_path = "C:/data/preprocessed_energy_dataset.csv"
data.to_csv(preprocessed_file_path, index=False)

# print success message

print("Preprocessing completed successfully. Preprocessed dataset saved to:", preprocessed_file_path)

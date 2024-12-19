import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# load the enhanced dataset

file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data = pd.read_csv(file_path)

# define target variable and features

print("\nDefining target and features...")
target = "CO2_Emissions"
features = [
    'Energy_Consumption', 'Renewable_Percentage', 'Fossil_Percentage',
    'Energy_Consumption_Per_Capita', 'Emissions_Intensity',
    'Population', 'GDP', 'Urbanization_Rate', 'Energy_Intensity'
]

X = data[features]
y = data[target]

# split the data into training and testing sets

print("\nSplitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train a random forest regressor

print("\nTraining Random Forest Regressor...")
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# make predictions

print("\nMaking predictions on the test set...")
y_pred = model.predict(X_test)

# evaluate model performance

print("\nEvaluating model performance...")
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# save the trained model

import joblib
model_file_path = "C:/data/random_forest_model.pkl"
joblib.dump(model, model_file_path)

# print success message

print("Model training completed successfully. Model saved to:", model_file_path)

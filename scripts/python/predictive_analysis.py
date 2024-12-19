import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# load the enhanced dataset

file_path = "C:/data/feature_enhanced_energy_dataset.csv"
data = pd.read_csv(file_path)

# define target variable and features

print("\nDefining target and features...")
target = 'High_Renewable_Adoption'
features = ['Energy_Consumption', 'Fossil_Percentage', 'Population', 
            'Urbanization_Rate', 'Energy_Intensity']
X = data[features]
y = data[target]

# ensure the target variable has at least two classes
if len(np.unique(y)) < 2:
    raise ValueError("The target variable must have at least two classes for classification.")

# split the data into training and testing sets

print("\nSplitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# check class distribution in training data
if len(np.unique(y_train)) < 2:
    raise ValueError("Training data must have at least two classes after splitting.")

# train a gradient boosting classifier

print("\nTraining Gradient Boosting Classifier...")
model = GradientBoostingClassifier(random_state=42)
model.fit(X_train, y_train)

# make predictions and evaluate the model

print("\nMaking predictions...")
y_pred = model.predict(X_test)

print("\nEvaluating model...")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# print success message

print("Predictive analysis completed successfully.")


# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# save the model to disk

# Step 2: Load the data
data = pd.read_csv('Data.csv')

# Step 3: Preprocess the data
# Handle missing values
data = data.dropna()

# Encode categorical variables
#data['Gener'] = pd.factorize(data['Gener'])[0]

# Normalize numeric features
# data['SNDD'] = (data['SNDD'] - data['SNDD'].mean()) / data['SNDD'].std()

# Step 4: Split the data
X = data.drop('Stress', axis=1)
y = data['Stress']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Build the model
clf = DecisionTreeClassifier(max_depth=3, min_samples_split=2, min_samples_leaf=1)

# Step 6: Train the model
clf.fit(X_train, y_train)

filename = 'decision_tree_model.sav'
joblib.dump(clf, filename)

# Step 7: Evaluate the model
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted'))
print("Recall:", recall_score(y_test, y_pred, average='weighted'))
print("F1-score:", f1_score(y_test, y_pred, average='weighted'))

# Step 8: Predict the stress values
# load the model from disk
loaded_model = joblib.load(filename)
new_data = pd.DataFrame({'Gener': [2], 'SNDD': [100.89195955], 'Age': [25]})
#new_data['Gener'] = pd.factorize(new_data['Gener'])[0]
#new_data['SNDD'] = (new_data['SNDD'] - data['SNDD'].mean()) / data['SNDD'].std()
prediction = loaded_model.predict(new_data)
print("Predicted stress value:", prediction)

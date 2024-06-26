# -*- coding: utf-8 -*-
"""sales_task_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DGSywoY1JwG-9G5At8HXLkyeAeZcssVq
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('advertising.csv')

print("Dataset information:")
print(data.info())
print("\nSummary statistics:")
print(data.describe())
print("\nFirst few rows of the dataset:")
print(data.head())

sns.pairplot(data)
plt.title('Pairplot of Advertising Data')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

print("\nMissing values in the dataset:")
print(data.isnull().sum())

X = data.drop('Sales', axis=1)
y = data['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("R-squared (R2 Score):", r2)

new_data = pd.DataFrame({'TV': [100], 'Radio': [25], 'Newspaper': [10]})
predicted_sales = model.predict(new_data)
print("\nPredicted Sales:", predicted_sales[0])
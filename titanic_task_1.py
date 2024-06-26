# -*- coding: utf-8 -*-
"""titanic_task_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K_2iuT1Hq5Vfd9AzkveHtHXRaR0YKFgo
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('titanic.csv')

data.head()

data.fillna(method='ffill', inplace=True)

data = pd.get_dummies(data, columns=['Sex', 'Embarked'])

X = data.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
y = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

y_pred

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

survived_passengers = data.loc[y_test.index[y_pred == 1]]

print("Details of passengers who survived:")
print(survived_passengers)
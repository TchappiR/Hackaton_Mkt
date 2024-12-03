# sourcery skip: pandas-avoid-inplace
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVR
pd.set_option('display.max_rows', None)

# preparation de la data base
data_base = pd.read_csv("database.csv")

print(type(data_base.columns))

(data_base.shape)
print(data_base.head())

# Nettoyage de la base de donnée
data_clean = data_base.drop(["ID","Education", "Marital_Status", "Year_Birth", "Z_CostContact", "Complain"], axis=1)

# Gestion des valeurs manquantes
(data_clean.isnull().sum(axis=0))

data_clean.dropna(inplace= True)

(data_clean.isnull().sum(axis=0))
(data_clean.info())

# Changement des types
data_clean["Dt_Customer"] = pd.to_datetime(data_clean["Dt_Customer"], errors='coerce')
#(data_clean.info())

#Séparation de la base de donnée

split_index = int(len(data_clean) * 0.75)
train_dataframe = data_clean.iloc[ : split_index]
test_dataframe = data_clean.iloc[split_index : ]

x_train = train_dataframe.drop(columns=["Response", "Dt_Customer"], axis=1)
y_train = (train_dataframe["Response"]).to_numpy().reshape(-1,1)

x_test = test_dataframe.drop(columns=["Response", "Dt_Customer"], axis=1)
y_test = (test_dataframe["Response"]).to_numpy().reshape(-1,1)

#Regression Logistique

model =LogisticRegression()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

print(classification_report(y_test, y_predict))
print(f"Précision : {accuracy_score(y_test, y_predict)}")

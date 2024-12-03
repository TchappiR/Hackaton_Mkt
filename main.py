# sourcery skip: pandas-avoid-inplace
import pandas as pd
import numpy as np

# preparation de la data base

data_base = pd.read_csv("database.csv")
#print(data_base.shape())
#print(data_base.info())

# Nettoyage de la base de donnée

data_clean = data_base.drop(["ID","Education", "Marital_Status", "Year_Birth", "Z_CostContact", "Complain"], axis=1)

# Gestion des valeurs manquantes

(data_clean.isnull().sum(axis=0))

data_clean.dropna(inplace= True)

(data_clean.isnull().sum(axis=0))
(data_clean.info())

# Changement des types

data_clean["Dt_Customer"] = pd.to_datetime(data_clean["Dt_Customer"], errors='coerce')
(data_clean.info())





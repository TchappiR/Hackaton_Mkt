import pandas as pd
import numpy as np

# preparation de la data base

data_base = pd.read_csv("database.csv")
print(data_base.shape())
print(data_base.info())

# Nettoyage de la base de donnée

data_clean = data_base.drop(["ID","Education", "Marital_Status", "Year_Birth", "Z_CostContact", "Complain", "Dt_Customer"], axis=1)




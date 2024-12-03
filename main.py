# sourcery skip: pandas-avoid-inplace
import pandas as pd

# preparation de la data base
data_base = pd.read_csv("database.csv")

(data_base.shape)
(data_base.info())

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

#Séparation de la base de donnée

def split_data(dataframe):
    split_index = int(len(dataframe) * 0.75)
    train_dataframe = dataframe.iloc[ : split_index]
    test_dataframe = dataframe.iloc[split_index : ]

    x_train = train_dataframe.drop(columns = ["Response"])
    y_train = train_dataframe[ ["Response"] ]

    x_test = test_dataframe.drop(columns = ["Response"])
    y_test = test_dataframe[ ["Response"] ]

    return x_train, y_train, x_test, y_test


split_data(data_base)




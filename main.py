import pandas as pd
import numpy as np

# preparation de la data base

data_base = pd.read_csv("database.csv")
print(data_base.info())
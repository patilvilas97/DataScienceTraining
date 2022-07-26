import pandas as pd
import numpy as np

data = pd.read_csv("Stores.csv")
print(data.shape)
print(data.describe())
print(data.isnull().sum())
print(data.tail(5))

data.drop_duplicates(inplace = True)

print(data.shape)
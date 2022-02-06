import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("National_Stock_Exchange_of_India_Ltd.csv")
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 10840)
pd.set_option('display.width', 2000)
print(data['Open'].unique);

print(data.isnull().sum())
def HandleOpen(value):
    if ',' in value:
        value = str(value).replace(',', '')
        # value = str(value).split(',')
        # value = value[0] + value[1]
        return float(value)
    else :
        return float(value)

data.Open = data['Open'].apply(HandleOpen)
print(data.head())
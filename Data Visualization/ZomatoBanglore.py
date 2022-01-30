import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("zomato.csv")
# print(data.shape)
data.drop_duplicates(inplace=True)
# print(data.shape)

data.drop(columns=['url', 'address','book_table','phone','menu_item','reviews_list','listed_in(city)'], axis=1, inplace=True)
print(data.shape)
print(data.isnull().sum())

def cleanRate(series):
    series = series.replace("/5", "", inplace=True)
    # print(series)
    return float(series)
print(data['rate'].unique())
data[data['rate']].fillna(data.mean())
print(data.isnull().sum())
data['rate'] = data['rate'].apply(lambda x: str(x).replace('/5', '')if '/5' in str(x) else str(x))
data['rate'] = data['rate'].apply(lambda x: str(x).replace('NEW', '')if 'NEW' in str(x) else str(x))
data['rate'] = data['rate'].apply(lambda x: str(x).replace('-', '')if '-' in str(x) else str(x))
data['rate'] = data['rate'].apply(lambda x: float(x))
print(data.isnull().sum())
print(data['rate'].dtype)
# series = 4.1/5
# series = series.replace("/5", "", inplace=True)
# print(series)
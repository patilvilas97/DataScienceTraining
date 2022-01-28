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

data['rate'] = data['rate'].apply(cleanRate(series))
# data.rate = data['rate'].transform(inpute_median)
print(data.isnull().sum())
print(data.describe())
# series = 4.1/5
# series = series.replace("/5", "", inplace=True)
# print(series)
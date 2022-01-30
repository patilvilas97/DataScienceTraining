import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("zomato.csv")
# print(data.shape)
data.drop_duplicates(inplace=True)
# print(data.shape)

data.drop(columns=['url', 'address','book_table','phone','menu_item','reviews_list','listed_in(city)'], axis=1, inplace=True)
print(data.shape)
# print(data.isnull().sum())

def handleRate(value):
    if(value == 'NEW' or value == '-'):
        return np.nan
    else:
        value = str(value).split('/')
        value = value[0]
        return float(value)

data['rate'] = data['rate'].apply(handleRate)
data['rate'] = data['rate'].fillna(data['rate'].mean())

print(data['approx_cost(for two people)'].unique())
def handleApproxCost(value):
    if ',' in str(value):
        value = str(value).split(',')
        value = value[0] + value[1]
        return float(value)
    elif value == 'nan' :
        value = data['approx_cost(for two people)'].median()
        return float(value)
    return float(value)
data['approx_cost(for two people)'] = data['approx_cost(for two people)'].apply(handleApproxCost)
print(data['approx_cost(for two people)'].unique())
# data['approx_cost(for two people)']= data['approx_cost(for two people)'].fillna(data['approx_cost(for two people)'].mean())
print(data.isnull().sum())
data.dropna(inplace=True)
print(data.isnull().sum())
print(data['location'].unique())
# print(data['rate'].dtype)
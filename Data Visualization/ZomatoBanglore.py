import pandas as pd
import numpy as np

data=pd.read_csv("ZomatoBanglore.csv")
print(data.shape)
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 10840)
pd.set_option('display.width', 2000)
print(data.head(10))
print(data.tail(10))
threshold = len(data)*0.1
print(threshold)
# data.drop(columns=['Zero'],axis=1,inplace=True)
data.drop(columns=['zero.2','zero.3','zero.4','zero.5','zero.6','zero.7','zero.8','zero.9'],axis=1, inplace=True)
print(data.sum())
print(data.shape)
print(data.tail(10))
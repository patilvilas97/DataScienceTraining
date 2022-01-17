import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("googleplaystore.csv")

# print(data.shape)
print(data.describe())
print(data[data['Rating'] > 5])
data.drop([10472],inplace=True)             ##Dropping the row having rating more than 5
print(data[10470:10475])                    ## Verifying whther dropped or not
print(data.info())
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 10840)
pd.set_option('display.width', 2000)


threshold = len(data)*0.1                                   ##Defining the Threshold ex 10%
data.dropna(thresh=threshold,axis=1, inplace=True)          ##Dropping the column having empty cells more than 90%
print(data.isnull().sum())                                  ##Checking the sum of the Empty Cells

def impute_median(series):
    return series.fillna(series.median())
data.Rating = data['Rating'].transform(impute_median)

print(data.isnull().sum())
data['Type'].fillna(str(data['Type'].mode().values[0]), inplace = True)
data['Current Ver'].fillna(str(data['Current Ver'].mode().values[0]), inplace = True)
data['Android Ver'].fillna(str(data['Android Ver'].mode().values[0]), inplace = True)
print(data.isnull().sum())
print(data['Current Ver'].mode())
print(data['Android Ver'].mode())
print(data.head(2000))
print(data.describe())


data['Price'] = data['Price'].apply(lambda x: str(x).replace('$', '')if '$' in str(x) else str(x))
data['Price'] = data['Price'].apply(lambda x: float(x))
data['Reviews'] = pd.to_numeric(data['Reviews'], errors='coerce')

data['Installs'] = data['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else str(x))
data['Installs'] = data['Installs'].apply(lambda x: str(x).replace(',', '')if ',' in str(x) else str(x))
data['Installs'] = data['Installs'].apply(lambda x:float(x))
print(data.head(10))
print(data.describe())
# data.boxplot()
# plt.show()
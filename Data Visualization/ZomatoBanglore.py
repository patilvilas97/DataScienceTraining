import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("zomato.csv")
data.rename(columns= {'approx_cost(for two people)':'approx_cost','listed_in(type)' : 'type'}, inplace=True )


pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 10840)
pd.set_option('display.width', 2000)
print(data.head())

data.drop_duplicates(inplace=True)
# print(data.shape)

data.drop(columns=['url', 'address','book_table','phone','menu_item','reviews_list','listed_in(city)', 'dish_liked'], axis=1, inplace=True)
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

# print(data['approx_cost(for two people)'].unique())
def handleApproxCost(value):
    if ',' in str(value):
        value = str(value).split(',')
        value = value[0] + value[1]
        return float(value)
    elif value == 'nan' :
        value = data['approx_cost'].median()
        return float(value)
    return float(value)
data['approx_cost'] = data['approx_cost'].apply(handleApproxCost)
print(data.head())
# data['approx_cost(for two people)']= data['approx_cost(for two people)'].fillna(data['approx_cost(for two people)'].mean())
# print(data.isnull().sum())
data.dropna(inplace=True)
# print(data.isnull().sum())
print(data.describe())
# print(data['rate'].dtype)


def handleLocation(value):
    if 'Koramangala' in value :
        value = 'Koramangala'
        return value
    else :
        return value

print(data['type'].unique())
data['location'] = data['location'].apply(handleLocation)
print(data['location'].unique())


# Koramangala
#
grp = data.groupby('location')
x = grp['rate'].agg(np.mean)
y = grp['votes'].agg(np.sum)

plt.figure(figsize=(16,9))
plt.plot(x, 'rD')
plt.title('Ratings as per location')
plt.xlabel('Locations')
plt.ylabel('Rating')
plt.xticks(rotation=90)
# plt.show()

plt.figure(figsize=(16,9))
plt.plot(y, linewidth=2 , color = 'blue')
plt.title('Total Votes as per location')
plt.xlabel('Locations')
plt.ylabel('Votes')
plt.xticks(rotation=90)
plt.show()


grp = data.groupby('')



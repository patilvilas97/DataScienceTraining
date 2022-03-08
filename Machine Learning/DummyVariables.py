import pandas as pd
from sklearn import linear_model

data = pd.read_csv('homeprices2.csv')
print(data)

dummies = pd.get_dummies(data.town)

mergedData = pd.concat([data,dummies], axis=1)

mergedData.drop(columns=['town','west windsor'], inplace=True)

print(mergedData)

model = linear_model.LinearRegression()
model.fit(mergedData[['area', 'monroe township', 'robinsville']],data['price'])
print(model.predict([[3600,0,1]]))
print(model.predict([[3600,0,0]]))
print(model.score(mergedData[['area', 'monroe township', 'robinsville']],data['price']))

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

data1 = data
data1.town = le.fit_transform(data1['town'])
print(data1)

x = data1[['town', 'area']].values
y = data.price.values

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
# print(x[:,0])
# print()
z = ohe.fit_transform(x).toarray()
print(z)


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
print(model.predict([[5000,0,0]]))
print(model.score(mergedData[['area', 'monroe township', 'robinsville']],data['price']))


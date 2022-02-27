import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle

data = pd.read_csv('homeprices.csv')
print(data)

model = linear_model.LinearRegression()
model.fit(data[['area']], data.price)

print(model.coef_)
print(model.intercept_)
print(model.predict([[5000]]))

with open('homepricesModel', 'wb') as f:
    pickle.dump(model, f)
with open('homepricesModel', 'rb') as f:
    mp = pickle.load(f)
    print(mp.predict([[5000]]))

print(mp.predict([[3000]]))


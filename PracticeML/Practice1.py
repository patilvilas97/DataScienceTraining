#Trying to Practice the Linear Regression Algorith for Handson
import pandas as pd
import numpy as np
import math
from sklearn import linear_model as lm

data = pd.read_csv(r"C:\Users\patil\Desktop\Programs\DataScienceTraining\Machine Learning\homeprices1.csv")
print(data)

median_bedrooms = math.floor(data['bedrooms'].median())
data.fillna(median_bedrooms, inplace=True)
print(data)

reg = lm.LinearRegression()
reg.fit(data[['area','bedrooms','age']], data['price'])
print(reg.predict([[8000, 3, 80]]))

print(reg.coef_)
print(reg.intercept_)
print(reg.score(data[['area','bedrooms','age']], data['price']))



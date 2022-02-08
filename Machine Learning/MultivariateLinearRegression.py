import numpy as np
import pandas as pd
from sklearn import linear_model as lm
import math
import matplotlib.pyplot as plt
data = pd.read_csv("homeprices1.csv")
print(data)
bedrooms = data.bedrooms.median()
median_bedrooms = math.floor(bedrooms)
data['bedrooms'] = data['bedrooms'].fillna(median_bedrooms)
print(data)


reg = lm.LinearRegression()
reg.fit(data[['area','bedrooms', 'age']], data['price'])
print(reg.predict([[3200,4,18]]))
print(reg.coef_)
print(reg.intercept_)

print(reg.predict([[5000,5,20]]))


# plt.plot(data['area','bedrooms','age'], reg.predict(data[['area','bedrooms','age']]))
# plt.show()
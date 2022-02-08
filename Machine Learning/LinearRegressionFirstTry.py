##Linear Regression

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model as lm

data = pd.read_csv('homeprices.csv')
print(data)

plt.scatter(data.area,data.price,color='red', marker='+')

reg = lm.LinearRegression()
reg.fit(data[['area']], data.price)
plt.plot(data.area, reg.predict(data[['area']]), color='red')
print(reg.predict([[5000]]))
print(reg.coef_)
print(reg.intercept_)

data1 = pd.read_csv('areas.csv')
print(data1)
p = reg.predict(data1)
data1['prices'] = p
print(data1)

data1.to_csv('HousePricePrediction.csv', index = False)
plt.show()
plt.show()
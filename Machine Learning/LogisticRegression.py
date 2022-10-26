import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model as lm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv("insurance_data.csv")
print(data)
plt.scatter(data['age'], data['bought_insurance'], marker='+')
# plt.show()

x=data[['age']]
y=data['bought_insurance']

reg = lm.LinearRegression()
reg.fit(x,y)

plt.xlabel("Age")
# plt.plot(data['age'],reg.predict(x), color='red')

Xtrain,Xtest,Ytrain,Ytest=train_test_split(x,y,test_size=0.2)


print(len(Xtrain))
print(len(Xtest))
print(len(Ytrain))
print(len(Ytest))

model=lm.LinearRegression()
model.fit(Xtrain,Ytrain)
print(model.predict(Xtest))
print(model.score(Xtest,Ytest))

print("--------------Logistic--------------")
model1 = LogisticRegression()
model1.fit(Xtrain,Ytrain)
print(model1.predict(Xtest))
print(model1.score(Xtest,Ytest))


plt.plot(data['age'], model1.predict(x))
plt.show()



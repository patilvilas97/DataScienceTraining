import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("carprices.csv")
print(data)

plt.xlabel = "Price"
plt.ylabel = "Mileage"
plt.scatter(data['Mileage'], data['Sell Price($)'])


data = data.rename(columns={'Age(yrs)' : 'Age', 'Sell Price($)' : "SellPrice"})


x = data[['Mileage', 'Age']]
y = data['SellPrice']

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
print("------------xTrain----------------")
print(x_train)
print("----------xTest----------------")
print(x_test)

model = LinearRegression()
model.fit(x_train,y_train)
abc = model.predict(x_test)
print(abc)
print(model.score(x_test,y_test))

plt.show()
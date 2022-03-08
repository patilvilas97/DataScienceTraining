import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("carprices.csv")
print(data)

plt.scatter(data['Mileage'], data['Sell Price($)'])
plt.show()
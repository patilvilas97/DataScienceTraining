import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("National_Stock_Exchange_of_India_Ltd.csv")
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 10840)
pd.set_option('display.width', 2000)
print(data['Open'].unique);

print(data.isnull().sum())
def HandleComma(value):
    if ',' in value:
        value = str(value).replace(',', '')
        # value = str(value).split(',')
        # value = value[0] + value[1]
        return float(value)
    else :
        return float(value)

data.Open = data['Open'].apply(HandleComma)
data.High = data['High'].apply(HandleComma)
data.Low = data['Low'].apply(HandleComma)
data.LTP = data['LTP'].apply(HandleComma)
# data['Chng'] = data['Chng'].apply(HandleComma)
# data['Volume (lacs)'] = data['Volume (lacs)'].apply(HandleComma)
data['Turnover (crs.)'] = data['Turnover (crs.)'].apply(HandleComma)
data['52w H'] = data['52w H'].apply(HandleComma)
data['52w L'] = data['52w L'].apply(HandleComma)
# data['365 d % chng'] = data['365 d % chng'].apply(HandleComma)
# data['30 d % chng'] = data['30 d % chng'].apply(HandleComma)
print(data)
print(data.describe())

grp = data.groupby(['Symbol'])
x = grp['52w H'].agg(np.mean)
plt.plot(x, linewidth=2, color='red')
plt.xticks(rotation=90)
# plt.show()
#

data.plot.bar(y=['52w H', '52w L'], x='Symbol')
plt.title('52 weeks Comparision')
plt.ylabel("Price")
plt.xlabel('Stocks')
# plt.show()


data.plot.bar(x='Symbol', y='% Chng')
plt.title('Percentage in Change')
plt.xlabel('Stocks')
plt.ylabel('Percentage in Change')
plt.show()
# plt.plot(x=data[
# ])


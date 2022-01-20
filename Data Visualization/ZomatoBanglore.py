import pandas as pd
import numpy as np

data=pd.read_csv("ZomatoBanglore.csv")
print(data.shape)
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 10840)
pd.set_option('display.width', 2000)
print(data.head(10))
print(data.tail(10))
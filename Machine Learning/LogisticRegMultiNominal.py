import pandas as pd

data = pd.read_csv("HR_comma_sep.csv")

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 15000)
pd.set_option('display.width', 2000)
print(data)
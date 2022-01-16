import pandas as pd
data = pd.read_csv("weather.csv", skiprows=1)                                   #To Skip the first row of the csv file
data = pd.read_csv("weather.csv", na_values=["n.a", "not available"])           #To Rename n.a and not available files as NaN
print(data)
data.to_csv("new.csv")
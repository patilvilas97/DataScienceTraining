import pandas as pd
import numpy as np

print(pd.__version__)

df = pd.read_csv("weather.csv")                                 ##Read the input csv file
print(df)

print(df.shape)                                                 ##print the number of rows and colums

(rows,columns) = df.shape                                       ##(tuple)returns values are stored in the respective variable
print(rows)
print(columns)

print(df.head())                                                ##print 5 columns from the top
print(df.head(2))                                               ##We can pass the number of columns tobe printed

print(df.tail())                                                ##print 5 columns from the bottom
print(df.tail(2))                                               ##We can pass number of columns tobe printed

print(df[2:5])                                                  ##will print the row number from2 to 4

print(df.columns)                                               ##will return the columns
print(df.Rainfall)                                              ##will print only the required column

print(np.max(df))                                               ##using numpy with pandas

print(df.Temp9am.min())                                         ##To print minimum without numpy

print(df.Temp9am.max())                                         ##To print maximum without numpy

print(df.describe())                                            ##To find the statistics of the column containing integers

my_list = [1,2,3,4,5,6,7,8,9,0]

pandas_list = pd.Series(my_list)                                ##Intializing pandas series

print(my_list)
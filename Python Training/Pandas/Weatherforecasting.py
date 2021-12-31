import pandas as pd

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
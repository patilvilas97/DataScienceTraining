import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##Step : 1 Reading the data and studying the data{
data = pd.read_csv("googleplaystore.csv")
print(data.shape)                                                   ##Finding the number of rows and columns
# print(data.describe())
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 10840)
pd.set_option('display.width', 2000)
##}Step:1 Ends      This step only involves some print function and doesnt include any actions

##Step : 2 Data Cleaning{
##After studying the data we can easily conclude some conclusion, based on that conclusions we can take actions to clean the dataset

# print(data[data['Rating'] > 5])
data.drop([10472],inplace=True)                                     ##Dropping the row having rating more than 5
# print(data[10470:10475])                                          ##Verifying whether dropped or not
# print(data.info())

threshold = len(data)*0.1                                           ##Defining the Threshold ex 10%
data.dropna(thresh=threshold,axis=1, inplace=True)                  ##Dropping the column having empty cells more than 90% i.e 100%-threshold
# print(data.isnull().sum())                                        ##Checking the sum of the Empty Cells

def impute_median(series):                                          ##Defined the function to fill the empty cells in Rating with
    return series.fillna(series.median())                           ##median of all the remaining values
data.Rating = data['Rating'].transform(impute_median)

# print(data.isnull().sum())
data['Type'].fillna(str(data['Type'].mode().values[0]), inplace = True)
data['Current Ver'].fillna(str(data['Current Ver'].mode().values[0]), inplace = True)
data['Android Ver'].fillna(str(data['Android Ver'].mode().values[0]), inplace = True)
# print(data.isnull().sum())
# print(data['Current Ver'].mode())
# print(data['Android Ver'].mode())
# print(data.head(2000))
# print(data.describe())

##Cleaning the data and removing unwanted signs such as ',' '$' from the dataset to convert them into numeric values so we can plot some graphs
data['Price'] = data['Price'].apply(lambda x: str(x).replace('$', '')if '$' in str(x) else str(x))      ##Removing $
data['Price'] = data['Price'].apply(lambda x: float(x))
data['Reviews'] = pd.to_numeric(data['Reviews'], errors='coerce')

data['Installs'] = data['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else str(x))   ##Removing + and ,
data['Installs'] = data['Installs'].apply(lambda x: str(x).replace(',', '')if ',' in str(x) else str(x))
data['Installs'] = data['Installs'].apply(lambda x:float(x))

# print(data.describe())                                            ##Checking whether the required fields are converted to numeric or not
##Step 2 Ends

##Step : 3 Data Visualization
grp = data.groupby('Category')                                      ##Grouping the required dataset into category
x=grp['Rating'].agg(np.mean)                                        ##x will  refer the mean of Rating of each category
y=grp['Price'].agg(np.sum)                                          ##y will  refer the total Price of each category
z=grp['Reviews'].agg(np.mean)                                       ##z will  refer the mean of Reviews of each category

plt.figure(figsize=(16,9))                                          ##Ploting a grpah for category vs rating
plt.plot(x, 'rD', color='blue')
plt.title('Category wise Rating')
plt.xlabel('Category')
plt.ylabel('Ratings')
plt.xticks(rotation=90)

# plt.show()
# print(y)
# print(x)
# print(z)

plt.figure(figsize=(16,9))                                          ##Ploting a grpah for category vs PriceTotal
plt.plot(y, 'r--', color='blue')
plt.title('Category wise TotalPrice')
plt.xlabel('Category')
plt.ylabel('PriceTotal')
plt.xticks(rotation=90)

# plt.show()

plt.figure(figsize=(16,9))                                          ##Ploting a grpah for category vs Reviews
plt.plot(z, 'rD', color='green')
plt.title('Category wise Reviews')
plt.xlabel('Category')
plt.ylabel('Reviews')
plt.xticks(rotation=90)

plt.show()
##Step 3 Ends
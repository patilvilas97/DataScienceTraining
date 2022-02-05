#Given in the CSV file is the data for number of Banglore Restaurants on Zomato, By studying the given data, Analyze the
#statistics and do conclude.

import pandas as pd                                                                                                       #Importing the required Libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##Reading the input file and setting the dsiplay options
data = pd.read_csv("zomato.csv")                                                                                        #Importing the data
data.rename(columns= {'approx_cost(for two people)':'approx_cost','listed_in(type)' : 'type'}, inplace=True )           ##Renaming the columns
pd.set_option('display.max_columns', 20)                                                                                #Adding the display specifications
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 10840)
pd.set_option('display.width', 2000)
# print(data.head())                                                                                                    #Printing the first five elements to get some idea about the data

##Dropping the COlumns
data.drop_duplicates(inplace=True)                                                                                      #Deleting Duplicate rows
# print(data.shape)
data.drop(columns=['url', 'address','phone','menu_item','reviews_list','listed_in(city)', 'dish_liked'], axis=1, inplace=True)  #Deleting unwanted Columns
# print(data.shape)
# print(data.isnull().sum())                                                                                            #Printing the null values


#Handling the Rate Column
def handleRate(value):                                                                                                  #{Handling the column 'RATE', removing spaces
    if(value == 'NEW' or value == '-'):                                                                                 #and returning the float values to  the dataframe
        return np.nan                                                                                                   #Also filling the improper values with null values
    else:                                                                                                               #as it is easier to handle null values
        value = str(value).split('/')
        value = value[0]
        return float(value)

data['rate'] = data['rate'].apply(handleRate)
data['rate'] = data['rate'].fillna(data['rate'].mean())                                                                 #Filling the null values with mean of the column rate


##Handling the Approximate Cost Column
# print(data['approx_cost'].unique())                                                                                   #Printing unique values from the respective column
def handleApproxCost(value):
    if ',' in str(value):                                                                                               #Handling the 'APPROX_COST' column and removing ','
        value = str(value).split(',')                                                                                   #from the values and returning float values
        value = value[0] + value[1]
        return float(value)
    elif value == 'nan' :
        value = data['approx_cost'].median()                                                                            #filling the null values with median
        return float(value)
    return float(value)
data['approx_cost'] = data['approx_cost'].apply(handleApproxCost)
# print(data.head())
# print(data.isnull().sum())
data.dropna(inplace=True)                                                                                               #Dropping the rows containing null values
# print(data.isnull().sum())
print(data.head())                                                                                                      #Describing the statistic for the dataframe
# print(data['rest_type'].value_counts())


##Handling the rest Type column
restType = data['rest_type'].value_counts(ascending=False)
restTypeLessThan1000 = restType[restType < 1000]
def handleRestType(value):
    if (value in restTypeLessThan1000):
        return 'Other Restaurants'
    else:
        return value
data['rest_type'] = data['rest_type'].apply(handleRestType)
# print(data['location'].value_counts())

##Handling the Cuisines Column
cuisines = data['cuisines'].value_counts(ascending=False)
cuisinesLessThan100 = cuisines[cuisines<100]
def handleCuisines(value):
    if value in cuisinesLessThan100:
        return 'Other Cuisines'
    else:
        return value

data['cuisines'] = data['cuisines'].apply(handleCuisines)
# print(data['cuisines'].value_counts())


##Handling the Location Column
location = data['location'].value_counts(ascending=False)
locationLessThan300 = location[location<300]

def handleLocation(value):                                                                                              #Handling the column 'LOCATION' merging some locations
    if value in locationLessThan300 :                                                                                  #which are similar to each others
        return 'Other Location'
    else :
        return value
# print(data['type'].unique())                                                                                          #Printing the Unique values from the column 'TYPE'
data['location'] = data['location'].apply(handleLocation)
# print(data['location'].value_counts())

##Data Cleaning has been done.

##Data Visualisation Started
plt.figure(figsize=(15,10))
# plt.figimage(data.shape,origin='upper',resize=True)
sns.countplot(data['location'])
plt.title("Count of Restaurants according to Location")
plt.xticks(rotation=90)


plt.figure(figsize=(15,10))
sns.countplot(data['online_order'])

plt.figure(figsize=(15,10))
sns.countplot(data['book_table'])

print(data.head())
plt.figure(figsize=(15,10))
sns.boxplot(data=data, x = 'online_order', y = 'rate')

plt.figure(figsize=(15,10))
plt.title("Comparing restaurants on the basis of book table Facility")
sns.boxplot(data=data, x='book_table', y='rate')
# plt.show()

data1 = data.groupby(['location', 'online_order'])['name'].count()
data1.to_csv("location_online.csv")
data1 = pd.read_csv("location_online.csv")
data1 = pd.pivot_table(data1, values=None, index=['location'],columns=['online_order'],fill_value=0, aggfunc=np.sum)
print(data1)
data1.plot(kind='bar')
plt.show()




grp = data.groupby('location')                                                                                        #Grouping the data as per location
x = grp['rate'].agg(np.mean)
y = grp['votes'].agg(np.sum)

plt.figure(figsize=(16,9))
plt.plot(x, 'rD')
plt.title('Ratings as per location')
plt.xlabel('Locations')
plt.ylabel('Rating')
plt.xticks(rotation=90)
# plt.show()

# plt.figure(figsize=(16,9))
# plt.plot(y, linewidth=2 , color = 'blue')
# plt.title('Total Votes as per location')
# plt.xlabel('Locations')
# plt.ylabel('Votes')
# plt.xticks(rotation=90)
# plt.show()


# grp = data.groupby('type')
# x = grp['rate'].mean
# plt.plot(x,'rD', color = 'blue')
# plt.show()
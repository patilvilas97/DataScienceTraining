import pandas as pd
from pandas_profiling import ProfileReport

data=pd.read_csv("googleplaystore.csv")

##Pandas Profile is used to create a html report who will readily provide all the data analysis of the dataset
profile = ProfileReport(data)
profile.to_file(output_file="googleplaystore.html")
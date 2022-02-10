import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from word2number import w2n

data = pd.read_csv("hiring.csv")
# print(data)

data['experience'].fillna('zero', inplace=True)
data.rename(columns={"test_score(out of 10)":"TestScore/10","interview_score(out of 10)":"InterviewScore/10" }, inplace=True)
data['TestScore/10'].fillna(data["TestScore/10"].median(), inplace=True)
print(data)
data['experience'] = data['experience'].apply(w2n.word_to_num)
print(data)

reg = linear_model.LinearRegression()
reg.fit(data[['experience', 'TestScore/10', 'InterviewScore/10']],data['salary($)'])
print(reg.coef_)
print(reg.intercept_)
print(reg.predict([[2,10,8]]))
print(reg.predict([[1,10,10]]))
import pandas as pd
from sklearn import linear_model

data = pd.read_csv("test_scores.csv")
print(data)

def gradientDescent(x,y):

    m_curr = b_curr = 0;
    iterations = 1000
    learning_rate = 0.1
    n = len(x)
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        # cost = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m : {}, b : {}, iterations {}".format(m_curr, b_curr, i))



gradientDescent(data.math,data.cs)
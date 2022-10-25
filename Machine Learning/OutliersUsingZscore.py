import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [10, 22, 3, 5, 6, 7, 8, 20, 7, 34, 2, 9, 10, 12, 15, 16 ,17 ,12, 14, 18, 19, 12, 11, 107, 12, 13, 12, 15, 107, 112]
outliers = []

def detect_outliers(data):
    threshold = 3
    mean = np.mean(data)
    print(mean)
    std = np.std(data)
    print(std)

    for i in data:
        zScore = (i-mean)/3
        if np.abs(zScore) > threshold:
            outliers.append(i)
    return outliers

detect_outliers(data)
print(outliers)


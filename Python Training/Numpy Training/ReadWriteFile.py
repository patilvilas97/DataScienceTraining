import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr)

np.savetxt("test.txt", arr)                             ##save the data in a txt file

arr2 = np.loadtxt("test.txt")                           ##Load the data from txt file
print(arr2)
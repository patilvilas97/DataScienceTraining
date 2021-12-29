import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print(arr.dtype)                                        ##Printing Data Type of array
print(arr[0,1,2])                                       ##Arrays Indexing
print(arr[1,1,1])

print(arr[-1,-1,-1])                                    ##Printing Last element of the array
import numpy as np

arr1 = np.array([1,2,1.3,4,2,], dtype=float)                     ##Initializing the array
print(arr1)
print(np.reciprocal(arr1))                           ##Creating reciprocals of the elements in array
print(np.reciprocal(arr1))

arr2 = np.array([23,56,78,22,98])                               ##initalizing the array
print(arr1+arr2)                                                ## Adding the arrays

print(arr1*arr2)                                                ##Multiplying the arrays

print(arr1/arr2)                                                ##Dividing two arrays

print(arr1.ndim)                                         ##To print the dimensions

print(arr1.size)                                         ##To count the number of elements present in the array

print(arr1.shape)                                        ##To print the row and column count of the array

arr= np.zeros((3,3))                                       ## initializing all the elements with zeroes

print(arr)

arr= np.ones((3,3))                                       ## initializing all the elements with ones

print(arr)

arr3=np.arange(1,10)                                    ##Create an array with elements 1 to 9

print(arr3)

arr3=np.arange(1,10,2)                                  ##create an array with increament of 2 from 1 upto 9

print(arr3)

arr3=np.linspace(1,5,20)                                ##will create 20 numbers between 1 and 5

print(arr3)

print(arr)

print(arr.ravel())                                      ##will convert any dimensional array to 1D

print(arr3.min())                                       ##To find the min from the array

print(arr3.max())                                       ##To find the max from the array

print(arr3.sum())                                       ##To sum up the array
arr[0,2]=7
arr[1,1]=8
print(arr.sum(axis=1))                                  ##Will sum up the rows and colums


arr5=np.ones((3,4))
print(arr5)
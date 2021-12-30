import numpy as np                              #importing Numpy Package and renaming it as np

numbers = np.array([1,2,3,4,5])                 ##Creating arrays anda adding values
print(numbers)
print(type(numbers))


print(numbers[0])                               ##Printing Independently
print(numbers[3])

for i in numbers:                               ##Prinitng all the values from arrays
    print(i, end=" ")
print()
for i in range(len(numbers)):
    print("Index Value:", i,"Value:",numbers[i])

arr=np.array("Vilas")
for i in arr.flat:
    print(i)
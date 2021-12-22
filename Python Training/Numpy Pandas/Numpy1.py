import numpy as np

new_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(new_matrix)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[[1, 2, 3], [4, 5, 6],[1,2,3]]], [[[1, 2, 3], [4, 5, 6],[7,8,9]]]])

print(a.ndim)
print(b.ndim)
print(c)
print(c.ndim)
print(d)
print(d.ndim)

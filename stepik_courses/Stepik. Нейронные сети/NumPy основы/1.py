import numpy as np

arr1 = np.eye(3, 4) * 2
arr2 = np.eye(3, 4, +1)

print(arr1+arr2)

import numpy as np

X = np.array([1,1,1,60,50,75])
X = X.reshape(2,3)
X = X.T

print(X)
y = np.array([10,7,12]).T

step1 = X.T.dot(X)
step2 = np.linalg.inv(step1)
step3 = step2.dot(X.T)
print(b)

b = step3.dot(y)




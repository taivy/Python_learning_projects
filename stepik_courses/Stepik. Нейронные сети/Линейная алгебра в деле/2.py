import urllib
from urllib import request
import numpy as np

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

y = np.array(data[:,0])

X = data.copy()
X[:,0] = 1
X = np.array(X)

step1 = X.T.dot(X)
step2 = np.linalg.inv(step1)
step3 = step2.dot(X.T)

b = step3.dot(y)
print(*b)

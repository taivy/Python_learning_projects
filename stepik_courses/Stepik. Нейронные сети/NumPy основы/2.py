import numpy as np
import random

w = np.array(random.sample(range(1000), 12))
w = w.reshape((2,2,3))

print(w.reshape(12, 1))

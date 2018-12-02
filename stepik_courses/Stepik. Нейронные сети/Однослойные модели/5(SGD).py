# -*- coding: utf-8 -*-


import numpy as np

def SGD(self, X, y, batch_size, learning_rate=0.1, eps=1e-6, max_steps=200):
    cnt = 1
    xy = np.column_stack((y, X))
    np.random.shuffle(xy)
    while cnt < max_steps:
        np.random.shuffle(xy)
        Xcalc = xy[0:batch_size, 1:]
        ycalc = xy[0:batch_size, 0:1]
        if self.update_mini_batch(Xcalc, ycalc, learning_rate, eps) == 1:
            return 1
        else:
            cnt += 1
            np.random.shuffle(xy)
    return 0
    

def update_mini_batch(self, X, y, learning_rate, eps):
    grad = compute_grad_analytically(self, X, y)
    j_1 = J_quadratic(self, X, y)
    self.w += -(learning_rate * grad)
    j_2 = J_quadratic(self, X, y)
    delta = j_1 - j_2
    if delta < eps:
        return 1
    else: 
        return 0





'''
не сходится на 5 тесте

import numpy as np

def SGD(self, X, y, batch_size, learning_rate=0.1, eps=1e-6, max_steps=200):
    cnt = 1
    cur_batches = 0
    xy = np.hstack((y, X))
    np.random.shuffle(xy)
    while cnt < max_steps:
        Xcalc = xy[cur_batches:cur_batches + batch_size, 1:]
        ycalc = xy[cur_batches:cur_batches + batch_size, 0:1]
        if self.update_mini_batch(Xcalc, ycalc, learning_rate, eps) == 1:
            return 1
        cnt += 1
        cur_batches += 1
    return 0

def update_mini_batch(self, X, y, learning_rate, eps):
    grad = compute_grad_analytically(self, X, y)
    j_1 = J_quadratic(self, X, y)
    self.w += -(learning_rate * grad)
    j_2 = J_quadratic(self, X, y)
    delta = j_1 - j_2
    if delta < eps:
        return 1
    else: 
        return 0
'''
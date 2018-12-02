# -*- coding: utf-8 -*-

import numpy as np

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
    
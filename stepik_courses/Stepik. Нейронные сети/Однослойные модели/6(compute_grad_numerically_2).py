# -*- coding: utf-8 -*-

import numpy as np

def compute_grad_numerically_2(neuron, X, y, J=J_quadratic, eps=10e-2):
    w_0 = neuron.w
    num_grad = np.zeros(w_0.shape)
    
    for i in range(len(w_0)):
        
        old_wi = neuron.w[i].copy()
        
        neuron.w[i] += eps
        j1 = J(neuron, X, y)
        neuron.w[i] = old_wi
        
        neuron.w[i] -= eps
        j2 = J(neuron, X, y)
        
        num_grad[i] = (j1 - j2)/(2*eps)
        
        neuron.w[i] = old_wi
        
    return num_grad

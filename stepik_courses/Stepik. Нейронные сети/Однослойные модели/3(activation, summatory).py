# -*- coding: utf-8 -*-

import numpy as np

def summatory(self, input_matrix):
        self.summatory_activation = input_matrix.dot(self.w)
        return self.summatory_activation

def activation(self, summatory_activation):
    return np.apply_along_axis(self.activation_function, 1, summatory_activation)

def vectorized_forward_pass(self, input_matrix):
    return self.activation(self.summatory(input_matrix))
import numpy as np

def vectorized_forward_pass(self, input_matrix):        
    result = input_matrix.dot(self.w)
    result += self.b
    result = result > 0
    return result


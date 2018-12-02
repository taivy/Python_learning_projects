import numpy as np

def train_on_single_example(self, example, y):
    y_ = self.w.T.dot(example) + self.b
    y_ = y_ > 0
    error = y - y_
    deltw = error*(example)
    self.w += deltw
    self.b += error

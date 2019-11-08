import numpy as np

def array_sum_to_one(array):
    '''
    '''
    return np.array(array) / np.array(array).sum(keepdims=1)
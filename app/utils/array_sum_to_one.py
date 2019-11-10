import numpy as np


def array_sum_to_one(array: list):
    """
    Adjust a list of values so that if we sum this list the result is one.

    Parameters
    ----------
    array : list
        list of values to adjust

    Returns
    -------
    numpy.array
        Number array which sum to one
    """
    return np.array(array) / np.array(array).sum(keepdims=1)

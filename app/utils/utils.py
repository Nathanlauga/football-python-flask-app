import numpy as np
import zipfile

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


def to_percent(proba: float, decimals=2):
    """
    Convert a probability to percentage

    Parameters
    ----------
    proba : float
        probability to convert to percentage
    decimals : int
        number of decimals to keep

    Returns
    -------
    float
        Percentage with n decimals
    """
    return (proba*100).round(decimals)


def list_to_list_two_tuples(values: list):
    """
    Convert a list of values to a list of tuples with for each
    value twice that same value
    e.g. [1,2,3] ==> [(1,1),(2,2),(3,3)]

    Parameters
    ----------
    values : list
        list of values to convert into tuples

    Returns
    -------
    list
        list of tuples with twice the same value for each tuple
    """
    return [(val, val) for val in values]


def exists(var):
    """
    Return a boolean value that indicate if a variable exists or not.

    Parameters
    ----------
    var
        Variable to test

    Returns
    -------
    bool
        Boolean that indicate the existance or not of the variable
    """
    try:
        var
    except NameError:
        return False
    else:
        return True


class OpenFile:
    """
    Class that open a file and close it at the end

    Attributes
    ----------
    filename : str
        file name
    mode : str
        mode for open() method
    """
    def __init__(self, filename: str, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()


def unzip(path: str, file_name: str):
    """

    """
    with zipfile.ZipFile(path+file_name, 'r') as zip_ref:
        zip_ref.extractall(path)
        zip_ref.close()
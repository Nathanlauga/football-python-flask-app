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

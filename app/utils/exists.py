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
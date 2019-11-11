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

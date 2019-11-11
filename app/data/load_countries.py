import pandas as pd


def load_countries(path: str):
    """
    Load the file 'countries.json' that contains all countries and 
    the flag svg file

    Parameters
    ----------
    path : str
        path to the directory which contains the json file

    Returns
    -------
    pd.Series
        countries name with their flag svg name
    """
    return pd.read_json(path+'countries.json', orient='index', typ='series')

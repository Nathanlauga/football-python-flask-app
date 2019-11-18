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


def load_results(path: str):
    """
    Load the file 'results.csv' that contains all international games
    since the beginning of this model

    Parameters
    ----------
    path : str
        path to the directory which contains the csv file

    Returns
    -------
    pd.DataFrame
        all international games since 2019-11-14
    """
    return pd.read_csv(path+'results.csv')


def load_predictions(path: str):
    """
    Load the file 'results_pred.csv' that contains all predictions for 
    international games since the beginning of this model

    Parameters
    ----------
    path : str
        path to the directory which contains the csv file

    Returns
    -------
    pd.DataFrame
        all prediction for international games since 2019-11-14
    """
    return pd.read_csv(path+'results_pred.csv')

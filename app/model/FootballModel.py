import pickle
import pandas as pd
import numpy as np
from scipy.stats import poisson


class FootballModel:
    """
    Model that predict a game result between
    2 internationals football teams
    """

    def __init__(self, path: str):
        self.model = self.load_model(path)

    @staticmethod
    def load_model(path: str):
        """
        """
        with open(path, 'rb') as file:
            model = pickle.load(file)
        return model

    def predict_avg_score(self, game):
        """
        """
        return self.model.predict(game).values[0]
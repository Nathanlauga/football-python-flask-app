import pickle
import pandas as pd
import numpy as np
from scipy.stats import poisson


class FootballModel:
    '''Model that predict a game result between 
    2 internationals football teams
    '''

    def __init__(self, path: str):
        self.model = self.load_model(path)

    def load_model(self, path: str):
        '''
        '''
        model = pickle.load(open(path, 'rb'))
        return model

    def predict_avg_score(self, game):
        '''
        '''
        avg_score = self.model.predict(game).values[0]
        return avg_score
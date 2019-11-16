import pandas as pd
import numpy as np
import pickle
from scipy.stats import poisson

from ..utils import array_sum_to_one, exists, to_percent, OpenFile

from enum import Enum


class ResultType(Enum):
    WIN_TEAM_1 = 1
    DRAW = 2
    WIN_TEAM_2 = 3


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
        with OpenFile(path, 'rb') as file:
            model = pickle.load(file)
        return model

    def predict_avg_score(self, game):
        """
        """
        return self.model.predict(game).values[0]


class Team:
    ''' 
    Class containing team information for a game.

    Attributes
    ----------
    name : str
        Full name of the team
    avg_goals : float
        Average number of goals 
    proba_goals : list
        List of scoring probability, the index correspond 
        to the the number of goals

    Methods
    -------
    compute_proba_goals(max_goals)
        Given a max number of goals it computes a poisson distribution
        based on the avg_goals attribute and as a result it gives the
        score probability for 0 to the maximumn number of goals 

    '''

    def __init__(self, name: str):
        self.name = name
        self.avg_goals = 0
        self.proba_goals = []

    def compute_proba_goals(self, max_goals: int):
        '''
        Given a max number of goals it computes a poisson distribution
        based on the avg_goals attribute and as a result it gives the
        score probability for 0 to the maximumn number of goals 

        Parameters
        ----------
        max_goals : int
            the maximum number of goals 
        '''
        self.proba_goals = [poisson.pmf(i, self.avg_goals)
                            for i in range(0, max_goals+1)]
        self.proba_goals = list(array_sum_to_one(self.proba_goals))


class Game:
    '''
    '''

    def __init__(self, model: FootballModel, team_1: str, team_2: str, max_goals=20):
        self.team_1 = Team(name=team_1)
        self.team_2 = Team(name=team_2)
        self.model = model
        self.max_goals = max_goals

    def format_game(self, team_1: Team, team_2: Team):
        '''
        '''
        game = pd.DataFrame(
            data={'team': team_1.name, 'opponent': team_2.name},
            index=[1])
        return game

    def is_team_1(self, team: Team):
        '''
        '''
        return team.name == self.team_1.name

    def set_team_goals_proba(self, team: Team):
        '''
        '''
        if self.is_team_1(team):
            team_1, team_2 = self.team_1, self.team_2
        else:
            team_1, team_2 = self.team_2, self.team_1
        game = self.format_game(team_1=team_1, team_2=team_2)

        team.avg_goals = self.model.predict_avg_score(game)
        team.compute_proba_goals(max_goals=self.max_goals)

    def compute_result_proba(self):
        '''
        '''
        self.proba_team_1 = np.sum(np.tril(self.result_proba_matrix, -1))
        self.proba_draw = np.sum(np.diag(self.result_proba_matrix))
        self.proba_team_2 = np.sum(np.triu(self.result_proba_matrix, 1))

        self.proba_team_1 = to_percent(self.proba_team_1)
        self.proba_draw = to_percent(self.proba_draw)
        self.proba_team_2 = to_percent(self.proba_team_2)

    def set_result_attr(self, result_type: ResultType, winner, looser):
        '''
        '''
        self.result_type = result_type
        self.winner = winner
        self.looser = looser

    def set_result(self):
        '''
        '''
        if not exists(var=self.result):
            return
        if (self.result[0] > self.result[1]):
            self.set_result_attr(result_type=ResultType.WIN_TEAM_1,
                                 winner=self.team_1,
                                 looser=self.team_2)
        elif (self.result[0] == self.result[1]):
            self.set_result_attr(result_type=ResultType.DRAW,
                                 winner=None,
                                 looser=None)
        else:
            self.set_result_attr(result_type=ResultType.WIN_TEAM_2,
                                 winner=self.team_2,
                                 looser=self.team_1)

    def is_winner(self, team: Team):
        '''
        '''
        return team == self.winner

    def is_looser(self, team: Team):
        '''
        '''
        return team == self.looser

    def and_the_winner_is(self):
        '''
        '''
        self.result = np.where(self.result_proba_matrix ==
                               np.amax(self.result_proba_matrix))
        self.set_result()

    def compute_result(self):
        '''
        '''
        self.set_team_goals_proba(self.team_1)
        self.set_team_goals_proba(self.team_2)

        self.result_proba_matrix = np.outer(self.team_1.proba_goals,
                                            self.team_2.proba_goals)

        self.compute_result_proba()
        self.and_the_winner_is()

        for index, proba in np.ndenumerate(self.result_proba_matrix):
            self.result_proba_matrix[index] = to_percent(proba)

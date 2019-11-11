from scipy.stats import poisson
from ..utils import array_sum_to_one

class Team:
    ''' 
    '''

    def __init__(self, name: str):
        self.name = name
        self.avg_goals = 0
        self.proba_goals = []

    def compute_proba_goals(self, max_goals: int):
        '''
        '''
        self.proba_goals = [poisson.pmf(i, self.avg_goals) for i in range(0, max_goals+1)]
        self.proba_goals = list(array_sum_to_one(self.proba_goals))
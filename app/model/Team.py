from scipy.stats import poisson
from ..utils import array_sum_to_one

class Team:
    ''' 
    Class containing team information for a game.

    ...

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
        self.proba_goals = [poisson.pmf(i, self.avg_goals) for i in range(0, max_goals+1)]
        self.proba_goals = list(array_sum_to_one(self.proba_goals))
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import NoneOf, DataRequired
from ..utils import list_to_list_two_tuples


class IndexForm(FlaskForm):
    """
    Form on the index page.
    This form is compose of two select fields for each team.
    """

    team = SelectField('Team 1', [DataRequired(), NoneOf(
        ['Choose a country'], 'Invalid country.')])
    opponent = SelectField('Team 2', [DataRequired(), NoneOf(
        ['Choose a country'], 'Invalid country.')])
    submit = SubmitField('And the winner is...')

    def init_choice(self, choice: list, default_choice='Choose a country'):
        """
        Initialize the choice list for team and opponent SelectField
        and add a default value.

        Parameters
        ----------
        choice : list
            list of values to put in the choice attribute
        default_choice : str 
            default value for SelectField (the default is 'Choose a country').
        """
        if type(choice) != type(list()):
            choice = list(choice)
        choice = list_to_list_two_tuples([default_choice] + choice)
        self.team.choices = choice
        self.opponent.choices = choice

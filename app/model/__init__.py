# from .load_model import load_model
from .FootballModel import FootballModel
from .Game import Game
from .Team import Team
from app import app

model = FootballModel('app/model/'+app.config['MODEL_FILE'])
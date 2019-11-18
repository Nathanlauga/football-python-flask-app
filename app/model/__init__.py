from .model import FootballModel
from .model import Game
from .model import ModelPerformance
from .model import Team
from app import app

model = FootballModel('app/model/'+app.config['MODEL_FILE'])
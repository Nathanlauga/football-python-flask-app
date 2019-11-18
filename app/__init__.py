from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object("config.Config")

# Load the views
from app import views

# TODO : page config pour refresh matchs joués
# TODO : documentation du code
# TODO : inclure scrapping en code du module
# TODO : refractor
# TODO : page result avec recherche 
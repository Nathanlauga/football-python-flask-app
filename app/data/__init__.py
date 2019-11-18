from .data import load_countries
from .data import load_results
from .data import load_predictions

countries = load_countries(path='app/data/')
game_results = load_results(path='app/data/')
predictions = load_predictions(path='app/data/')
from flask import render_template, request
import pandas as pd

from .model import model, Game

from app import app


@app.route('/', methods=['GET', 'POST'])
def index():

    countries = pd.read_json('./app/static/data/countries.json', orient='index', typ='series')
    # pd.Series(team_list).to_json('teams.json')

    if request.method == 'POST':
        teams = request.form.to_dict()

        game = Game(model, team_1=teams['team'], team_2=teams['opponent'])
        game.compute_result()

        return render_template("index.html", teams=countries, game=game)

    return render_template("index.html", teams=countries)

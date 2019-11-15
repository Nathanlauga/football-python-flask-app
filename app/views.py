from flask import render_template, request
import pandas as pd
import json

from .model import model, Game
from .component import IndexForm
from .data import countries

from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    form.init_choice(countries.index.values)

    if request.method == 'POST':
        teams = request.form.to_dict()
        if form.validate():
            game = Game(model, team_1=teams['team'], team_2=teams['opponent'])
            game.compute_result()
            return render_template("index.html", teams=countries, form=form, game=game)

    return render_template("index.html", teams=countries, form=form)


@app.route('/game/<game>', methods=['GET', 'POST'])
def game(game):
    try:
        team, opponent = game.split('_')[0:2]
        if team not in countries.index or opponent not in countries.index:
            raise Exception('Not a valid country')
    except:
        return render_template("404.html")

    game = Game(model, team_1=team, team_2=opponent)
    game.compute_result()

    return render_template("game.html", game=game, teams=countries)

@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 
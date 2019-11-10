from flask import render_template, request, redirect, url_for, flash
import pandas as pd

from .model import model, Game
from .component import IndexForm

from app import app


@app.route('/', methods=['GET', 'POST'])
def index():

    countries = pd.read_json('./app/static/data/countries.json', orient='index', typ='series')

    form = IndexForm()
    form.init_choice(countries.index.values)

    if request.method == 'POST':
        teams = request.form.to_dict()
        if form.validate():
            game = Game(model, team_1=teams['team'], team_2=teams['opponent'])
            game.compute_result()
            return render_template("index.html", teams=countries, form=form, game=game)

    return render_template("index.html", teams=countries, form=form)

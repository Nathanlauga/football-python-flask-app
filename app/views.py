from flask import render_template, request
import pandas as pd
import json

from .model import model, Game
from .component import IndexForm
from .data import countries, results

from app import app


def predict_score_new_games(results):
    data = pd.read_csv('app/data/results_pred.csv')

    max_date = max(data['date']) if len(data) > 0 else '13-11-2019'
    results = results[results['date'] > max_date]
    pred_df = []
    if len(results) > 0:
        for index, row in results.iterrows():
            pred_row = row
            game = Game(model, row['home_team'], row['away_team'])
            pred_row['home_team_score'] = game.result[0][0]
            pred_row['away_team_score'] = game.result[1][0]
            pred_df += [pred_row.to_frame().T]

        pred_df = pd.concat(pred_df)
        pred_df.to_csv('app/data/results_pred.csv', index=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    form.init_choice(countries.index.values)
    predict_score_new_games(results)

    if request.method == 'POST':
        teams = request.form.to_dict()
        if form.validate():
            game = Game(model, team_1=teams['team'], team_2=teams['opponent'])
            # game.compute_result()
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
    # game.compute_result()

    return render_template("game.html", game=game, teams=countries)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

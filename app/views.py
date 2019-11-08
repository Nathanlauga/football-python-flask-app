from flask import render_template, request
import pandas as pd

from .model import model, Game

from app import app


@app.route('/', methods=['GET', 'POST'])
def index():

    games = pd.read_csv('./app/data/results.csv')
    team_list = pd.concat([games['home_team'], games['away_team']]
                          ).sort_values().unique()
    del games

    if request.method == 'POST':
        teams = request.form.to_dict()
        print(teams)
        teams = list(teams.values())

        game = Game(model, team_1=teams[0], team_2=teams[1])
        game.compute_result()
        
        # result = get_match_result(model, teams[0], teams[1])

        return render_template("index.html", teams=team_list, game=game)

    return render_template("index.html", teams=team_list)

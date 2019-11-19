import numpy as numpy
import pandas as pd
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import warnings
warnings.filterwarnings("ignore")


countries = pd.read_json('./app/data/'+'countries.json',
                         orient='index', typ='series')

def get_date(days: int):
    date = datetime.date.today() - datetime.timedelta(days=days)
    return date.strftime('%d-%m-%Y')


def format_game(game_html):
    team1 = game_html.find('span', class_='team1').text.strip()
    team2 = game_html.find('span', class_='team2').text.strip()
    match_info = game_html.find('span', class_='match_info')

    score1 = match_info['data-hscore']
    score2 = match_info['data-ascore']

    return [team1, score1, score2, team2]


i = 1
date = get_date(i)
min_date = '13-11-2019'
df = []

synonyms = pd.read_json('app/data/synonyms.json', orient='index', typ='series')

while date != min_date:
    url = 'https://livescore.football365.com/football/all/'+date

    # Get the html from the url
    html = urlopen(url)
    # Convert it to soup
    soup = BeautifulSoup(html, 'html.parser')

    # Get all game boxes
    game_boxes = soup.find_all('div', class_='match_table_block vevent')
    # Filter on international game
    international_game_boxes = [
        box for box in game_boxes if 'International' in box.text]

    games = []

    for box in international_game_boxes:
        games += box.find_all('div', class_='match_tabel_row')

    del game_boxes, international_game_boxes

    games = [format_game(game) + [date] for game in games]

    for game in games:
        if game[0] not in countries.index:
            game[0] = synonyms[game[0]]
        if game[3] not in countries.index:
            game[3] = synonyms[game[3]]

    df += games

    i += 1
    date = get_date(i)

data = pd.DataFrame(df, columns=['team_1','team_1_score','team_2_score','team_2','date'])
data.to_csv('app/data/results.csv',index=False)
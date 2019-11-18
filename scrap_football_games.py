from difflib import SequenceMatcher
import numpy as numpy
import pandas as pd
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import warnings
warnings.filterwarnings("ignore")


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def find_best_match(a, str_list):
    best_match, best_score = '', 0
    for elem in str_list:
        if any_word_same(a, elem):
            return elem

        score = similar(a.replace(' ', ''),
                        elem[4:-4].replace('-', ' ').replace(' ', ''))
        if best_score < score:
            best_match, best_score = elem, score
    return best_match


countries = pd.read_json('./app/data/'+'countries.json',
                         orient='index', typ='series')


def get_dupplicated_word():
    dup_word = pd.Series(
        [word for country in countries.index for word in country.split()]).value_counts()
    return list(dup_word[dup_word > 1].index.values) + ['North']


def any_word_same(first, second):
    dup_words = get_dupplicated_word()
    return any([f_word.upper() == s_word.upper() and f_word not in dup_words for s_word in second.split() for f_word in first.split()])


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
            game[0] = find_best_match(game[0], countries.index)
        if game[3] not in countries.index:
            game[3] = find_best_match(game[3], countries.index)

    df += games

    i += 1
    date = get_date(i)

data = pd.DataFrame(df, columns=['team_1','team_1_score','team_2_score','team_2','date'])
data.to_csv('app/data/results.csv',index=False)
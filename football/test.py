import sys
sys.path.append("c:\py\diploma\diplomWindows\diplom\project")
sys.path.append("/Users/alekseyiovchev/Python/diplomaMac/diplom/project/")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoUI.settings')

import django
django.setup()


import requests
from football.models import Scores


games_url = 'http://api.football-data.org/v4/matches/?dateFrom=2022-11-11&dateTo=2022-11-21'
request = requests.get(games_url,headers={'X-Auth-Token':'b5611168bafe4dd2a3fcc7b6b7e19e9a'})
result = request.json()['matches']
for match in result:
    print(
        match['id'],
        match['utcDate'],
        match['homeTeam']['shortName'],
        match['homeTeam']['crest'],
        '|',
        match['awayTeam']['shortName'],
        match['awayTeam']['crest'],
        match['score']['fullTime']['home'],
        '-',
        match['score']['fullTime']['away']
        )
    
    Scores.objects.create(
        id=match['id'],
        first_team=match['homeTeam']['shortName'],
        first_team_icon = match['homeTeam']['crest'],
        second_team=match['awayTeam']['shortName'],
        second_team_icon = match['awayTeam']['crest'],
        match_date=match['utcDate'],
        score_first_team=int(match['score']['fullTime']['home']),
        score_second_team=int(match['score']['fullTime']['away'])
        )
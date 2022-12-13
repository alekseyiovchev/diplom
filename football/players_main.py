import sys
sys.path.append("c:\py\diploma\diplomWindows\diplom\project")
sys.path.append("/Users/alekseyiovchev/Python/diplomaMac/diplom/project/")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoUI.settings')

import django
django.setup()


import requests
from football.models import Players


def run_players(result):
    for data in result:
        print(Players.objects.filter(id=data['id']))
        if not Players.objects.filter(id=data['id']):
            Players.objects.create(
                id=data['id'],
                first_team=data['homeTeam']['shortName'],
                first_team_icon = data['homeTeam']['crest'],
                second_team=data['awayTeam']['shortName'],
                second_team_icon = data['awayTeam']['crest'],
                data_date=data['utcDate'],
                score_first_team=int(data['score']['fullTime']['home']),
                score_second_team=int(data['score']['fullTime']['away'])
                )
            
            print(
            data['id'],
            data['utcDate'],
            data['homeTeam']['shortName'],
            data['homeTeam']['crest'],
            '|',
            data['awayTeam']['shortName'],
            data['awayTeam']['crest'],
            data['score']['fullTime']['home'],
            '-',
            data['score']['fullTime']['away']
            )
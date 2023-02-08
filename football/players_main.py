import sys
sys.path.append("c:\py\diploma\diplomWindows\diplom\project")
sys.path.append("/Users/alekseyiovchev/Python/diplomaMac/diplom/project/")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoUI.settings')

import django
django.setup()


import requests
from football.models import Players,Player_matches

def create_player(result):
    if not Players.objects.filter(id=result['id']):
        Players.objects.create(id=result['id'],name=result['name'],date_of_birth=result['dateOfBirth'],nationality=result['nationality'])
        print(result['id'],result['name'],result['dateOfBirth'],result['nationality'])

def player_matches(result,id):
    print(result)
    for data in result:
        
        if not Player_matches.objects.filter(id=data['id']):
            Player_matches.objects.create(
                player= Players(id=id),
                match_id=data['id'],
                first_team=data['homeTeam']['shortName'],
                first_team_icon = data['homeTeam']['crest'],
                second_team=data['awayTeam']['shortName'],
                second_team_icon = data['awayTeam']['crest'],
                match_date=data['utcDate'],
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
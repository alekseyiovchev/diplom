import sys
sys.path.append("c:\py\diploma\diplomWindows\diplom\project")
sys.path.append("/Users/alekseyiovchev/Python/diplomaMac/diplom/project/")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoUI.settings')

import django
django.setup()


import requests
from football.models import Scores


def run_scores(result):
    for match in result:
        print(Scores.objects.filter(id=match['id']))
        if not Scores.objects.filter(id=match['id']):
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
            
            # print(
            # match['id'],
            # match['utcDate'],
            # match['homeTeam']['shortName'],
            # match['homeTeam']['crest'],
            # '|',
            # match['awayTeam']['shortName'],
            # match['awayTeam']['crest'],
            # match['score']['fullTime']['home'],
            # '-',
            # match['score']['fullTime']['away']
            # )
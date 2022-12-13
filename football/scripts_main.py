import scores_main
import requests

import sys
sys.path.append("c:\py\diploma\diplomWindows\diplom\project")
sys.path.append("/Users/alekseyiovchev/Python/diplomaMac/diplom/project/")

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoUI.settings')

import django
django.setup()


import requests
from football.models import Scores,Players

games_url = 'http://api.football-data.org/v4/matches/?dateFrom=2022-11-21&dateTo=2022-11-30'
request = requests.get(games_url,headers={'X-Auth-Token':'b5611168bafe4dd2a3fcc7b6b7e19e9a'})
result = request.json()['matches']


if __name__ == "__main__":
    scores_main.run_scores(result)
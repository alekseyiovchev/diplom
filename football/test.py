import requests
import json
from models import Scores

games_url = 'http://api.football-data.org/v4/matches/?dateFrom=2022-11-11&dateTo=2022-11-21'
request = requests.get(games_url,headers={'X-Auth-Token':'b5611168bafe4dd2a3fcc7b6b7e19e9a'})
result = request.json()['matches']
for match in result:
    print(
        match['id'],
        match['utcDate'],
        match['homeTeam']['shortName'],
        '|',
        match['awayTeam']['shortName'],
        match['score']['fullTime']['home'],
        '-',
        match['score']['fullTime']['away']
        )
    
    Scores.objects.create(
        id=match['id'],
        first_team=match['homeTeam']['shortName'],
        second_team=match['awayTeam']['shortName'],
        
        )
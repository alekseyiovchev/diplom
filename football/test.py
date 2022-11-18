import requests
import json

games_url = 'http://api.football-data.org/v4/matches/?dateFrom=2022-11-10&dateTo=2022-11-17'
request = requests.get(games_url,headers={'X-Auth-Token':'b5611168bafe4dd2a3fcc7b6b7e19e9a'})
result = request.json()['matches']
for i in result:
    print(i['id'],i['utcDate'],i['homeTeam']['shortName'],'|',i['awayTeam']['shortName'],i['score']['fullTime']['home'],'-',i['score']['fullTime']['away'])

print('lesha2')
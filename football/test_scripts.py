import requests
import json


games_url = 'https://api.football-data.org/v4/persons/44/matches?status=FINISHED'
request = requests.get(games_url,headers={'X-Auth-Token':'b5611168bafe4dd2a3fcc7b6b7e19e9a'})
result = request.json()['person']

for i in result:
    # Scores.objects.create()
    print(i['id'],i['name'],i['dateOfBirth'],i['nationality'])
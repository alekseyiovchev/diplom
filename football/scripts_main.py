import scores_main
import players_main
import requests
from datetime import *

from football.models import Scores,Players

host = 'api.football-data.org/v4'
api = {'X-Auth-Token':'b5611168bafe4dd2a3fcc7b6b7e19e9a'}

# Scores
dateFrom = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")
dateTo = datetime.now().strftime("%Y-%m-%d")
games_url = f'http://{host}/matches/?dateFrom={dateFrom}&dateTo={dateTo}'

def get_info(url,data=None):
    request = requests.get(url,headers=api)
    result = request.json()[data]
    return result
    

if __name__ == "__main__":
    ## For whole scores

    scores_main.run_scores(get_info(games_url,data='matches'))


    ### For Players matches
    ids = list(Players.objects.all().values_list('id', flat=True))

    for id in ids:
        player_url = f'https://{host}/persons/{id}/matches?status=FINISHED'

        players_main.create_player(get_info(player_url,data='person'))
        players_main.player_matches(get_info(player_url,data='matches'),id)
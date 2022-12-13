import scores_main
import players_main
import requests

from football.models import Scores,Players

host = 'api.football-data.org/v4'
api = {'X-Auth-Token':'b5611168bafe4dd2a3fcc7b6b7e19e9a'}

# Scores
games_url = f'http://{host}/matches/?dateFrom=2022-11-05&dateTo=2022-11-12'

# Players
id = 2019
player_url = f'https://{host}/persons/{id}/matches?status=FINISHED'


def get_info(url,data=None):
    request = requests.get(url,headers=api)
    result = request.json()[data]
    return result
    

if __name__ == "__main__":
    # scores_main.run_scores(get_info(games_url,data='matches'))
    players_main.create_player(get_info(player_url,data='person'))
    players_main.player_matches(get_info(player_url,data='matches'),id)
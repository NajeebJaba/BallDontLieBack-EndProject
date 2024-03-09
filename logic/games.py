from infra.api_wrapper import BallDontLieAPI

class GamesData:
    def __init__(self, api_key):
        self.api = BallDontLieAPI(api_key)

    def get_games_list(self):
        response = self.api.get_games()
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(f"Failed to fetch games: {response.status_code}")
            return None
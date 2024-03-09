import requests


class BallDontLieAPI:
    BASE_URL = "https://api.balldontlie.io/v1"

    def __init__(self, api_key):
        self.headers = {'Authorization': f'Bearer {api_key}'}

    def get_players(self):
        return requests.get(f"{self.BASE_URL}/players")

    def get_teams(self):
        return requests.get(f"{self.BASE_URL}/teams")

    def get_games(self):
        return requests.get(f"{self.BASE_URL}/games", headers=self.headers)

    def get_stats(self):
        return requests.get(f"{self.BASE_URL}/stats", headers=self.headers)

    def get_player_by_id(self, player_id):
        return requests.get(f"{self.BASE_URL}/players/{player_id}")

    def get_team_by_id(self, team_id):
        return requests.get(f"{self.BASE_URL}/teams/{team_id}")





from infra.api_wrapper import BallDontLieAPI

class PlayerData:
    def __init__(self):
        self.api = BallDontLieAPI()

    def get_player_list(self):
        response = self.api.get_players()
        data = response.json() if response.ok else None
        print("Player List Data:", data)
        return data

    def get_player_details_by_id(self, player_id):
        response = self.api.get_player_by_id(player_id)
        return response.json() if response.ok else None

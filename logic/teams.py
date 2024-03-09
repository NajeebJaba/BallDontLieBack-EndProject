from infra.api_wrapper import BallDontLieAPI

class TeamData:
    def __init__(self):
        self.api = BallDontLieAPI()

    def get_team_list(self):
        response = self.api.get_teams()
        return response.json() if response.ok else None

    def get_team_details_by_id(self, team_id):
        response = self.api.get_team_by_id(team_id)
        return response.json() if response.ok else None

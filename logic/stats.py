from infra.api_wrapper import BallDontLieAPI


class StatsData:
    def __init__(self):
        self.api = BallDontLieAPI()

    def get_stats_list(self):
        response = self.api.get_stats()
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(f"Failed to fetch stats: {response.status_code}")
            return None
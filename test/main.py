import unittest
from logic.ballnotlie import BallDontLieData
import concurrent.futures


class TestBallDontLieAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_data = BallDontLieData()

    def test_get_players(self):
        data = self.api_data.get_player_list()
        self.assertIsNotNone(data)
        self.assertIn('data', data)

    def test_get_teams(self):
        data = self.api_data.get_team_list()
        self.assertIsNotNone(data)
        self.assertIn('data', data)




    def test_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.run_test_on_browser, browser): browser for browser in self.browsers}
            for future in concurrent.futures.as_completed(futures):
                browser = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    print(f'{browser} generated an exception: {exc}')
                else:
                    print(f'{browser} page title is {result}')


if __name__ == '__main__':
    unittest.main()


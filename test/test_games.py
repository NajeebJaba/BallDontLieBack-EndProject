import unittest
from logic.games import GamesData
import concurrent.futures


class TestGamesData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_key = '46e29623-4a45-46d5-83ca-8acc2be72534'
        cls.api_data = GamesData(cls.api_key)

    def test_get_games_list(self):
        games_list = self.api_data.get_games_list()
        self.assertIsNotNone(games_list, "API request did not return data.")
        self.assertIsInstance(games_list, list, "The data should be a list")

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

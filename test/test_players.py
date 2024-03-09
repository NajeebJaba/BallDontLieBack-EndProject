import unittest
from logic.players import PlayerData
import concurrent.futures


class TestPlayerData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.player_data = PlayerData()

    def test_get_player_list(self):
        data = self.player_data.get_player_list()
        self.assertIsNotNone(data)
        self.assertIn('data', data)

    def test_get_all_players_status(self):
        response = self.players_api.get_all_players()
        self.assertIsNotNone(response, "API request did not return data.")
        self.assertIn('data', response)

    def test_player_details(self):
        player_id = 1
        response = self.players_api.get_player_by_id(player_id)
        self.assertIsNotNone(response, "API request did not return data.")
        self.assertEqual(response['first_name'], "Alex")
        self.assertEqual(response['last_name'], "Abrines")
        self.assertEqual(response['college'], "FC Barcelona")

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

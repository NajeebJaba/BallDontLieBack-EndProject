import unittest
from logic.teams import TeamData
import concurrent.futures


class TestTeamData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.team_data = TeamData()

    def test_get_team_list(self):

        data = self.team_data.get_team_list()
        self.assertIsNotNone(data)
        self.assertIn('data', data)

    def test_get_all_teams_status(self):
        response = self.teams_api.get_all_teams()
        self.assertIsNotNone(response, "API request did not return data.")
        self.assertIn('data', response)

    def test_team_details(self):
        team_id = 1
        response = self.teams_api.get_team_by_id(team_id)
        self.assertIsNotNone(response, "API request did not return data.")
        self.assertEqual(response['city'], "Atlanta")
        self.assertEqual(response['name'], "Hawks")

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

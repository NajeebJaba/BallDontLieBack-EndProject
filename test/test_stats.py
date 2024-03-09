import unittest
from logic.stats import StatsData
import concurrent.futures


class TesStatsData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_key = '46e29623-4a45-46d5-83ca-8acc2be72534'
        cls.api_data = StatsData(cls.api_key)

    def test_get_stats_list(self):
        stats_list = self.api_data.get_stats_list()
        self.assertIsNotNone(stats_list, "API request did not return data.")
        self.assertIsInstance(stats_list, list, "The data should be a list")

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

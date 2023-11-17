import unittest
from stockData import get_Data

class proj3Test(unittest.TestCase):

    def test_symbol(self):
        # Valid symbols
        valid_symbols = ["AAPL", "GOOGL", "MSFT"]
        for symbol in valid_symbols:
            self.assertTrue(get_Data(symbol, "1", "1", "2000-01-01", "2022-01-02"))

    def test_chart(self):
        # Valid chart types
        valid_chart_types = ["1", "2"]
        for chart_type in valid_chart_types:
            self.assertTrue(get_Data("AAPL", chart_type, "1", "2000-01-01", "2022-01-02"))

    def test_time(self):
        # Valid time series
        valid_time_series = ["1", "2", "3", "4"]
        for time_series in valid_time_series:
            self.assertTrue(get_Data("AAPL", "1", time_series, "2000-01-01", "2022-01-02"))

    def test_start_date(self):
        # Valid start dates
        valid_start_dates = ["2022-01-01", "2023-11-17"]
        for start_date in valid_start_dates:
            self.assertTrue(get_Data("AAPL", "1", "1", start_date, "2022-01-02"))

    def test_end_date(self):
        # Valid end dates
        valid_end_dates = ["2022-01-02", "2023-11-18"]
        for end_date in valid_end_dates:
            self.assertTrue(get_Data("AAPL", "1", "1", "2000-01-01", end_date))

if __name__ == '__main__':
    unittest.main()

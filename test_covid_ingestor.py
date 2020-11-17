from unittest import TestCase
from covid_ingestor import CovidIngester
from pprint import pprint
import datetime as dt

class TestCovidIngester(TestCase):
    def test_get_cases_last_seven_days(self):
        covid_ing = CovidIngester()
        result_dict = covid_ing.get_cases_last_seven_days()
        #pprint(result_dict)
        yesterday = dt.date.today - dt.timedelta(days = 1)
        self.assertEqual(True, str(yesterday) in result_dict)
        


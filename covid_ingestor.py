import http.client
import ssl
import json
from pprint import pprint
import datetime as dt
from typing import Dict

class CovidIngester:
    def __init__(self):
        self.context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.context.verify_mode=ssl.CERT_NONE
        self.conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com",
                                                context=self.context)

        self.headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "fa62248741mshefc0e6d84a8ff27p137c99jsnf14b6972752a"
        }
    def get_cases_last_seven_days(self) -> Dict[str, int]:
        #get day's results and pack into dictionary, returns the dictionary
        today = dt.date.today()
        yesterday = today - dt.timedelta(days=1)
        result_dict = {}
        for days_back in range(1, 7):
            past_date = today - dt.timedelta(days = days_back)

            self.conn.request("GET", f"/history?country=usa&day={past_date}", headers=self.headers)
            res = self.conn.getresponse()
            data = res.read()
            json_string = data.decode("utf-8")
            covid_dict = json.loads(json_string)
            new_cases = int(covid_dict['response'][0]['cases']['new'])

            result_dict[str(past_date)] = new_cases

        return result_dict

    def ingest(self):

        self.conn.request("GET", "/statistics?country=USA", headers=self.headers)

        res = self.conn.getresponse()
        data = res.read()
        json_string = data.decode("utf-8")

        print(data.decode("utf-8"))

        covid_dict = json.loads(json_string)
        pprint(covid_dict)

        response_value = covid_dict["response"]
        response1 = response_value[0]
        cases_value = response1['cases']
        new_cases = cases_value['response'][0]["cases"]['new']
        pprint(new_cases)

        #pprint(response_value[0])
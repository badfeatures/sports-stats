import unittest
import requests
import time

from .. import StatsAPI

try:
    import config
except ImportError:
    raise Exception("You must have a config.py file in order to run the acceptance tests. Rename config.example.py to config.py and add your credentials.")


class TestRequest(unittest.TestCase):

    def test_trigger(self):

        api = StatsAPI(config.app_key, config.app_secret)
        resp = api.request('/decode/languages/')
        time.sleep(1)
        if resp.status_code == requests.codes.ok:
            assert True
        else:
            print resp.text
            assert False

    def test_trigger_with_rest_params(self):

        api = StatsAPI(config.app_key, config.app_secret)
        resp = api.request(
            '/stats/:sportName/:leagueAbbrev/dateDataUpdated/',
            {'sportName': 'football', 'leagueAbbrev': 'nfl'}
        )
        time.sleep(1)
        if resp.status_code == requests.codes.ok:
            assert True
        else:
            print resp.text
            assert False

    def test_trigger_with_rest_params_and_get_params(self):

        api = StatsAPI(config.app_key, config.app_secret)
        resp = api.request(
            '/stats/:sportName/:leagueAbbrev/events/',
            {'sportName': 'baseball', 'leagueAbbrev': 'mlb'},
            {'date': '2015-04-20'}
        )
        time.sleep(1)
        if resp.status_code == requests.codes.ok:
            assert True
        else:
            print resp.text
            assert False

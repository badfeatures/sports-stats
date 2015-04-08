import unittest, re, httplib, time, cgi, time

from .. import StatsAPI

try:
    import test_config
except ImportError:
    raise Exception("you must have a test_config.py file in order to run the acceptance tests. Rename test_config.example.py to test_config.py and add your credentials.")


class TestRequest(unittest.TestCase):

    def test_trigger(self):

        api = StatsAPI(test_config.app_key, test_config.app_secret)
        resp = api.request('/decode/languages/')
        time.sleep(1)
        if resp.status_code == 200:
            assert True
        else:
            assert False

    def test_trigger_with_rest_params(self):

        api = StatsAPI(test_config.app_key, test_config.app_secret)
        resp = api.request('/stats/:sportName/:leagueAbbrev/dateDataUpdated/', {'sportName': 'football', 'leagueAbbrev': 'nfl'})
        time.sleep(1)
        if resp.status_code == 200:
            assert True
        else:
            assert False
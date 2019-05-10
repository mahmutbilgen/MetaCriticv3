#!/usr/local/bin/python3

import requests
import unittest

import htmlparse.parser as p


class test_metacritic_availability(unittest.TestCase):
    def setUp(self):
        self.url = 'http://www.metacritic.com/game/playstation-4'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    def tearDown(self):
        pass

    def test_metacritic_com(self):
        resp = requests.get(self.url, headers=self.headers)
        assert resp.status_code == 200


class test_mcparser_state(unittest.TestCase):
    def setUp(self):
        self.m = p.HtmlParser()
        self.m.refresh_state()

    def tearDown(self):
        pass

    def test_check_games_list_size(self):
        print(len(self.m.mc_state))
        assert len(self.m.mc_state) == 10


if __name__ == '__main__':
    unittest.main()

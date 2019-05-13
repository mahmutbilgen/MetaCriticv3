#!/usr/local/bin/python3

import logging
import time

import requests
from bs4 import BeautifulSoup


class HtmlParser(object):

    def __init__(self):
        #self.url = 'http://www.metacritic.com/game/playstation-4'
        self.url = 'http://www.metacritic.com/game'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        self.last_update_ts = 0
        self.mc_state = []

    def refresh_state(self):
        resp = requests.get(self.url, headers=self.headers)
        if resp.status_code != 200:
            SystemExit(" did not receive http 200  code from Metacritic web site")
        else:
            self.last_update_ts = time.time()
            logging.info("Parsed Metacritic, timestamp: {0}".format(
                self.last_update_ts))

        """Parses HTML contents for the data we're interested in, 
        then returns a list of dictionaries containing the results"""
        soup = BeautifulSoup(resp.content, 'html.parser')
        products_html = soup.find_all("td", {"class": "clamp-summary-wrap"})
        for product_html in products_html:
            product_title_header = product_html.find("a", {"class": "title"})
            product_title = product_title_header.get_text().strip()
            product_score_span = product_html.find("div", {"class": "metascore_w large game positive"})
            product_score = product_score_span.get_text().strip()
            self.mc_state.append(({"title": product_title, "score": product_score}))

    def get_game(self, game_title):
        game = str(game_title).lower().strip()
        if time.time() - self.last_update_ts > 60:
            self.refresh_state()
        try:
            r = [i for i in self.mc_state if str(
                i["title"]).lower() == game][0]
            return r['title'], r['score']
        except LookupError:
            logging.warning(
                "Title not found in top 10: {0}".format(game_title))
        return (game_title, 'Not found')

    def get_all(self):
        if time.time() - self.last_update_ts > 60:
            self.refresh_state()
        return self.mc_state

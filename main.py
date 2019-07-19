#!/usr/bin/env python
import fire
import requests

DATA = "data"
DOLLAR_SIGN = "$"
FORWARD_SLASH = "/"
FUZZY_SEARCH = "https://api.scryfall.com/cards/named?fuzzy=%s"
NAME = "name"
PRICES = "prices"
PRINTS_SEARCH_URI = "prints_search_uri"
SET_NAME = "set_name"
SPACE = " "
TAB = "\t"
USD = "usd"
USD_FOIL = "usd_foil"


class Card:

    @staticmethod
    def search(name):
        # TODO: Need to figure out how to deal with spaces.
        response = requests.get(FUZZY_SEARCH % name)

        # TODO: Refactor all the print statements into a separate method.
        print(Card.__get_card_name(response))

        for set_name, card_prices_usd in Card.__get_card_set_names(response).items():
            normal_price = None
            foil_price = None

            print(TAB + set_name)

            if not card_prices_usd[0] is None:
                normal_price = card_prices_usd[0]
            else:
                normal_price = "N/A"

            if not card_prices_usd[1] is None:
                foil_price = card_prices_usd[1]
            else:
                foil_price = "N/A"

            print(TAB + TAB + DOLLAR_SIGN + normal_price + SPACE + FORWARD_SLASH + SPACE + DOLLAR_SIGN + foil_price)

    @staticmethod
    def __get_card_name(response):
        return response.json()[NAME]

    @staticmethod
    def __get_card_set_names(response):
        card_set_list = dict()
        prints_search_uri = response.json()[PRINTS_SEARCH_URI]

        card_sets_response = requests.get(prints_search_uri)

        for json in card_sets_response.json()[DATA]:
            # TODO: Pull these values into variables since its a little hard to read.
            card_set_list.update({json[SET_NAME]:[json[PRICES][USD], json[PRICES][USD_FOIL]]})

        return card_set_list


if __name__ == '__main__':
    fire.Fire(Card)

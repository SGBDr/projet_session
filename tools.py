"""
This module contain all utils fonction like requesting server or parsing date
"""

import json
import requests
import datetime

URL = "https://pax.ulaval.ca/action/"

def format_date(date):
    """
    Formating date to format requeste : datetime.date(xxx, xx, xx)
    """
    year, mouth, day = split_string_date_in_component(date)

    return f"datetime.date({year}, {mouth}, {day})"


def split_string_date_in_component(date):
    """
    From string, return int component (year, mouth, day)
    """

    return date.split("-")


def get_date_from_string(date):
    """
    From string goes to date
    """
    year, mouth, day = map(int, split_string_date_in_component(date))

    return datetime.date(year, mouth, day)


def request_historique_in_json_format(symbole, params):
    """
    Resuest data to the server with url and params
    return to json format
    """
    # creation of url
    temp_url = f'{URL}{symbole}/historique/'
    rps = requests.get(url=temp_url, params=params)

    return json.loads(rps.text)["historique"]

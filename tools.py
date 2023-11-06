"""
This module contain all utils fonction like requesting server or parsing date
"""

import json
import requests


def format_date(date):
    """
    Formating date to format requeste : datetime.date(xxx, xx, xx)
    """
    date_block = date.split("-")

    return f"datetime.date({date_block[0]}, {date_block[1]}, {date_block[2]})"


def request_information_in_json_format(url, params):
    """
    Resuest data to the server with url and params
    return to json format
    """
    rps = requests.get(url=url, params=params)

    return json.loads(rps.text)

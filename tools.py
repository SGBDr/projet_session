import requests
import json


def format_date(date):
    date_block = date.split("-")
    return f"datetime.date({date_block[0]}, {date_block[1]}, {date_block[2]})"


def request_information_in_json_format(url, params):
    rps = requests.get(url=url, params=params)
    return json.loads(rps.text)
import requests
import json
from colorama import Back, Style
from datetime import datetime


def get_results(url):
    request = requests.get(url)
    result = request.json()
    # print(json.dumps(result, indent=4))
    return result["data"]


def get_ticker(url):
    results = get_results(url)
    return results[0]


def get_coloured_text(text):
    color = Back.GREEN if (text > 0) else Back.RED
    return color + str(text) + Style.RESET_ALL


def get_date_time(unix_timestamp):
    date_time = datetime.fromtimestamp(unix_timestamp)\
        .strftime("%b %d, %Y at %I:%M%p")
    return Back.GREEN + str(date_time) + Style.RESET_ALL

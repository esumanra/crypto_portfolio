import pyttsx3
from datetime import datetime
import time
import helper_api as api


listings_url = "https://api.coinmarketcap.com/v2/listings/"
currency = "INR"
url_end = "?convert={}&structure=array".format(currency)
already_hit = []
symbol_id_pairs = {}
alert = pyttsx3.init()

listings_results = api.get_results(listings_url+url_end)

for item in listings_results:
    symbol_id_pairs[item['symbol']] = item['id']

print()
print("TRACKING FOR ALERTS...")
print()

while True:
    with open("alerts.txt") as inp:
        for line in inp:
            symbol, amount = line.split()

            ticker_url = "https://api.coinmarketcap.com/v2/ticker/{}/{}"\
                .format(symbol_id_pairs[symbol], url_end)

            ticker_results = api.get_ticker(ticker_url)

            _quotes = ticker_results['quotes']
            curr = _quotes['INR']
            symbol = ticker_results['symbol']
            price = curr['price']
            name = ticker_results['name']
            last_updated = ticker_results['last_updated']

            if float(price) >= float(amount) and symbol not in already_hit:
                alert_str = "{} hit {}".format(name, amount)
                alert.say(alert_str)
                alert.runAndWait()
                last_updated = datetime.fromtimestamp(last_updated).\
                    strftime('%B %d, %Y at %I:%M%p')
                print(alert_str)
                print()
                print(last_updated)
                print("-------------------------")
                already_hit.append(symbol)

    print("...")
    time.sleep(300) # 5 minutes until next currency update
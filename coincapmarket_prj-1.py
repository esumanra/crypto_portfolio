from prettytable import PrettyTable


import helper_api as api

listings_url = " https://api.coinmarketcap.com/v2/listings/"
currency = "INR"
url_end = "?convert={}&structure=array".format(currency)
symbol_id_pairs = {}

table = PrettyTable(['Currency', 'Amount', 'INR Value', 'Price', '1hr', '24hr', '7d'])

total_portfolio = 0.00
listings_results = api.get_results(listings_url)

for item in listings_results:
    symbol_id_pairs[item['symbol']] = item['id']

print()
print("My Crypto Currency Portfolio")
with open('portfolio.txt') as inp:
    for line in inp:
        symbol, amount = line.split()

        ticker_url = "https://api.coinmarketcap.com/v2/ticker/{}/{}". \
            format(symbol_id_pairs[symbol.upper()], url_end)

        ticker_results = api.get_ticker(ticker_url)

        curr_name = "{} ({})".format(ticker_results['name'], ticker_results['symbol'])
        price = round(ticker_results['quotes'][currency]['price'], 2)
        value = round(price * float(amount), 2)
        _quotes = ticker_results['quotes']
        hour = _quotes[currency]['percent_change_1h']
        day = _quotes[currency]['percent_change_24h']
        week = _quotes[currency]['percent_change_7d']
        last_updated = ticker_results['last_updated']

        hour_color = api.get_coloured_text(hour)
        day_color = api.get_coloured_text(day)
        week_color = api.get_coloured_text(week)

        row = [curr_name, amount, value, price, hour_color, day_color, week_color]
        table.add_row([it for it in row])

        total_portfolio += value

total_portfolio = round(total_portfolio, 2)
last_updated = api.get_date_time(last_updated)
print(table)
print()
print("Money value of your cyptocurrency is Rs.{}".format(api.get_coloured_text(total_portfolio)))
print()
print("Currency last updated on: {}".format(last_updated))


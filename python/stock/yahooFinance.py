import yfinance as yf
import json
import pandas as pd
import requests
import yahooquery as yq

def get_symbol(query, preferred_exchange='AMS'):
    try:
        data = yq.search(query)
    except ValueError: # Will catch JSONDecodeError
        print(query)
    else:
        quotes = data['quotes']
        if len(quotes) == 0:
            return 'No Symbol Found'

        symbol = quotes[0]['symbol']
        for quote in quotes:
            print("quote = ", quote)
            if cleanName(quote['longname']) == query.lower():
                symbol = quote['symbol']
                break
        return symbol


def cleanName(name):
    return name.replace(" inc", "").replace(" ltd", "").replace(",", "").replace(".", "").replace(" corporation", "").replace(" limited", "").lower()

test = 'Apple'
symbol = get_symbol(test)


ticker = yf.Ticker(symbol)

dat = ticker.history(period='1mo', interval='1d')
print(dat)
print(dat.to_json())
high = dat.get('High')
low = dat.get('Low')
print("help me")
i = 0
stock_list = list()
for date, val in high.items():
    stock_list.append((str(date.to_pydatetime()), (high[i], low[i])))
    i+=1

print(stock_list)
pogch = json.dumps(stock_list)
print(pogch)






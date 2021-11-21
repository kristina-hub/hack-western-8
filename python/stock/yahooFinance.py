import yfinance as yf
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

print(ticker.history(period='max'))

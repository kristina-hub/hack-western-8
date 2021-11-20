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
            if quote['exchange'] == preferred_exchange:
                symbol = quote['symbol']
                break
        return symbol

test = 'Apple'
symbol = get_symbol(test)


ticker = yf.Ticker(symbol)

print(ticker.history(period='max'))

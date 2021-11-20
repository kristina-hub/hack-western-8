import requests
import spacy
from bs4 import BeautifulSoup
from googlesearch import search
import yfinance as yf
import pandas as pd
import requests
import yahooquery as yq
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class DataResult:
    def __init__(self, url, company, ticker):
        self.url = url
        self.company = company
        self.ticker = ticker

    def __str__(self):
        return f'({self.ticker})'



def getNouns(title):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(title)
    #print("The nouns are:")
    return list(doc.noun_chunks)


# return list(doc.noun_chunks)

def get_symbol(query, preferred_exchange='AMS'):
    try:
        data = yq.search(query)
    except ValueError:  # Will catch JSONDecodeError
        print(query)
    else:
        quotes = data['quotes']
        if len(quotes) == 0:
            return 'No Symbol Found'

        symbol = "No Symbol Found"
        for quote in quotes:
            # print("quote = ", quote)
            try:
                if query.lower() in quote['longname'].lower():
                    symbol = quote['symbol']
                    break
            except:
                #print(quote)
                if query.lower() in quote['shortname'].lower():
                    symbol = quote['symbol']
                    break
        return symbol

def getFinanceData(symbol):
    ticker = yf.Ticker(symbol)
    return ticker.history(period='max')



# to search
# query = "large donations to mental health charity"
#query = "corporate donation to healthcare media"

query = "corporate donation to mental health media"

results = []

for url in search(query, tld="co.in", num=10, stop=20, pause=2):
    try:
        # making requests instance
        reqs = requests.get(url)

        # using the BeaitifulSoup module
        soup = BeautifulSoup(reqs.text, 'html.parser')

        # displaying the title
        #print("Title of the website is : ")

        title = soup.find('title').get_text()

        print(title)

        title = title.replace("/[^a-zA-Z ]/g", "").replace("|", "")

        nouns = getNouns(title)

        for noun in nouns:
            symbol = get_symbol(str(noun))
            #print(noun, " = ", symbol)
            if symbol != "No Symbol Found":
                print(noun, " = ", symbol)
                results.append(DataResult(url, noun, symbol))
    except:
        print("error, moving on")

    #print("END")
for result in results:
    print(result.url)
    print(result.company)
    print(getFinanceData(result.ticker))
#print("The end")

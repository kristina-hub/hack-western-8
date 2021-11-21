import json

from flask import Flask, render_template, request, url_for, redirect
from bs4 import BeautifulSoup
import requests

from python.Combined import getResultsFromQuery

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/query')
def query():
   return render_template('query.html')

@application.route('/query', methods=['POST'])
def my_form_post():
    text = request.form['query']
    query = text.upper()
	return query
	
    # data = parseQuery(query)
    # return redirect(url_for('stocks', data=data))
    # return parseQuery(query)
    
    # string = function(query)
    # input string into stocks.html
    # graph = function(query)
    # input graph into stocks.html
    

@application.route('/stocks', methods=['GET', 'POST'])
def stocks():
   return render_template('stocks.html')


# def parseQuery(queryterm):
#     searchterm = "news company donates to " + queryterm
#     datalist = getResultsFromQuery(searchterm, "1mo", "1d")
# 
#     jsonlist = list()
#     for lis in datalist:
#         url = lis[0]
#         companyName = lis[1]
#         dat = lis[2]
#         high = dat.get('High')
#         low = dat.get('Low')
# 
#         i = 0
#         stock_list = list()
#         for date, val in high.items():
#             stock_list.append((str(date.to_pydatetime()), (high[i], low[i])))
#             i += 1
#         jsonlist.append((companyName, stock_list))
# 
#     return json.dumps(jsonlist)

if __name__ == "__main__":
    application.run(debug=True)
    #print(parseQuery("hospital"))
'''
To test locally:
export FLASK_APP="application.py"
flask run
command shift R to reload static files
'''
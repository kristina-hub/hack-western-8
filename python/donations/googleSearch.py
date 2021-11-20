import requests
import spacy
from bs4 import BeautifulSoup
from googlesearch import search

def getNouns(title):
	nlp = spacy.load("en_core_web_sm")
	doc = nlp(title)
	print("The nouns are :")
	print(list(doc.noun_chunks))

# to search
query = "companies donating to mental health charity"

for url in search(query, tld="co.in", num=10, stop=20, pause=2):
	# making requests instance
	reqs = requests.get(url)

	# using the BeaitifulSoup module
	soup = BeautifulSoup(reqs.text, 'html.parser')

	# displaying the title
	print("Title of the website is : ")

	title = soup.find('title').get_text()

	print(title)

	getNouns(title)
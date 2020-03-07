import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import nltk.data
from nltk.tokenize import word_tokenize
nltk.download('punkt')


def getToolkit(url, toolkit_name):
    url = url.rstrip()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    soup = soup.find("div", class_="content")
    soup.find("ul", class_="breadcrumbs").decompose()

    text_arr = [t for t in soup.find_all(text=True) if t.parent.name is not "" ]
    text = ""
    for t in text_arr:
        text += t
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)

    text = ""
    for sentence in sentences:
        text += sentence.strip() + " "

    text = text.strip().lower()

    return text
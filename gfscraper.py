from bs4 import BeautifulSoup
import requests
import re

def gfscraper():
    fields = ['stock_price']
    while True:
        name = input("Stock Name:")
        url = 'https://www.google.com/finance?q={}'.format(name)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup.prettify())
        
        #Finding the damn stock price

        div = soup.find('div', {'id': 'price-panel'})
        span = div.find('span', attrs={'id':'ref_694653_l'})
        print( span.text)

gfscraper()

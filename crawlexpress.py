import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint


tulieu = []
phantich=[]

pages = np.arange(1,34)

for page in pages: 

  page = requests.get("https://vnexpress.net/the-gioi/tu-lieu-p" + str(page))

  soup_tulieu = BeautifulSoup(page.text, 'html.parser')
  news_tulieu = soup_tulieu.find_all('h2', class_='title-news')
  
  sleep(randint(2,10))

  for container in news_tulieu:

        name = container.a.text
        tulieu.append(name)

for page in pages: 

  page = requests.get("https://vnexpress.net/the-gioi/phan-tich-p" + str(page))

  soup_phantich = BeautifulSoup(page.text, 'html.parser')
  news_phantich = soup_phantich.find_all('h2', class_='title-news')
  
  sleep(randint(2,10))

  for container in news_phantich:

        name = container.a.text
        phantich.append(name)


new = pd.DataFrame({
'new': tulieu
,'phantich':phantich
})




# to move all your scraped data to a CSV file
new.to_csv('vnexpress.csv')
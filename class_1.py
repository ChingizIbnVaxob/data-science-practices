# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:40:34 2024

@author: INHA
"""

import math 
import datetime as dt

# hozir = dt.date.weekday()
# print(hozir)
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi, 10))


# tarjimon = Translator()

# msg = "Tarjima uchun so'z kiriting(chiqib ketish uchun  \"q\" deb yozing!): "

# while True:
#      text = input(msg)
#      if text == "q":
#          break
#      else:
#          tarjima = tarjimon.translate(text, src='uz', dest='en')
#          print(tarjima.text)
         
# matn_en = "Tsshkent is the capital of Uzbekistan"
# tarjima_uz = tarjimon.translate(matn_en, dest='uz')
# print(tarjima_uz.text)


import requests
from pprint import pprint
import googletrans
from bs4 import BeautifulSoup


sahifa = "https://kun.uz/news/main"
r=requests.get(sahifa)

# pprint(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title")
print(news[22].text)

country = "Uzbekistan"

url = "https://api.adviceslip.com/advice"
r = requests.get(url)

advice = r.json()['slip']['advice']

print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest='uz')

print(tarjima.text)


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
from wordcloud import WordCloud
import matplotlib.pyplot as plt


sahifa = "https://kun.uz/news/main"
r=requests.get(sahifa) 

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title")
matn = ""
for n in news: 
    matn+= n.text

# kerakmas so'zlar
stopwords = ["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]

# bulutni yaratamiz
wordcloud= WordCloud(width=1000, height=1000, background_color='white',
                       stopwords = stopwords, 
                       min_font_size = 20).generate(matn)

plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()






# pprint(r.text)

# bizga kerakli title ni kun .uz sahifasidan yuklab olish.
print(news[0].text)

country = "Uzbekistan"

url = "https://api.adviceslip.com/advice"
r = requests.get(url)

advice = r.json()['slip']['advice']

print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest='uz')

print(tarjima.text)


from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
# from uzwords import words


print(fuzz.ratio('Salom', 'Assalom'))
print(fuzz.ratio('salom', 'salim'))


import wx
from googletrans import Translator

tarjimon = Translator()
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Oʻzbek-Ingliz Lugʻat')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        
        my_btn = wx.Button(panel, label='TARJIMA')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        
        self.text_out = wx.TextCtrl(panel,style = wx.TE_READONLY)        
        my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)         
        panel.SetSizer(my_sizer)        
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:                       
            self.text_out.SetValue("Soʻz kiritmadingiz")
        else:
            tarjima = tarjimon.translate(value, src='uz', dest='en')
            self.text_out.SetValue(tarjima.text.capitalize()) 
    

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

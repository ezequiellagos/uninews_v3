from django.shortcuts import render
from news.models import News, University, Category
from .models import Scraper, ScrapersLog
from bs4 import BeautifulSoup

import unidecode
import threading
import logging
import feedparser
import urllib.request

def start_scraper(request):
    logging.basicConfig( level=logging.DEBUG, format='[%(levelname)s] - %(threadName)-10s : %(message)s')
    scraper_upla()
    return render(request, 'scraper/scraper.html')
    

# def search_formatter(text):
#     text = unidecode.unidecode(text).lower()
#     text = text.replace('"', "")
#     text = text.replace('?', "")
#     text = text.replace('¿', "")
#     text = text.replace(':', "")
#     text = text.replace('#', "")
#     text = text.replace('.', "")
#     text = text.replace(',', "")
#     text = text.replace(';', "")
#     text = text.replace('(', "")
#     text = text.replace(')', "")

#     return text

def date_format(date):
    return date

# Universidad de Playa Ancha
def scraper_upla():
    scraper = Scraper.objects.get(university__alias='UPLA')
    feed = feedparser.parse(scraper.url)

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        date = entry.published

        categories = []
        for category in entry.tags:
            categories.append(category.term)


        with urllib.request.urlopen(link) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')

            
        
        
        print(f'{link}')
        # logging.debug(f'{title}')



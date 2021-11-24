from django.shortcuts import render
# from news.models import News, University
# from bs4 import BeautifulSoup
# from .decorators import logging_decorator

# import unidecode
# import threading
# import logging

def start_scraper(request):
    # logging.basicConfig( level=logging.DEBUG, format='[%(levelname)s] - %(threadName)-10s : %(message)s')
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

# # Universidad de Playa Ancha
# @logging_decorator
# def scraper_upla():
#     pass

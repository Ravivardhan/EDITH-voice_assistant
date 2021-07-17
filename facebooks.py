import webbrowser
import urllib3
from bs4 import BeautifulSoup

def facebook():

        url = 'https://www.facebook.com/'
        webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(r'C:\Program Files\Mozilla Firefox\firefox.exe'))
        webbrowser.get('firefox').open(url)



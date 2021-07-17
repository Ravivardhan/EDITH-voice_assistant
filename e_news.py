import webbrowser
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
def today():
    one_year_from_now = datetime.datetime.now() + relativedelta(years=1)
    date_formated = one_year_from_now.strftime("%d/%m/%Y")
    newspaper(date_formated)





def newspaper(date):

        url = 'https://epaper.eenadu.net/Home/Index?date={}&eid=2&pid=1272425'.format(date)
        webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(r'C:\Program Files\Mozilla Firefox\firefox.exe'))
        webbrowser.get('firefox').open(url)

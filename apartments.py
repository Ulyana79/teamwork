import requests 
#from bs4 import BeautifulSoup

URL = 'https://www.avito.ru/balashiha/kvartiry/prodam/2-komnatnye-ASgBAQICAUSSA8YQAUDKCBSCWQ?i=1'
HEADERS = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'accept':'*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
    #return r.text

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.text)
    else:
        print('Error')    

parse()    


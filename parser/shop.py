from pprint import pprint
import requests
from bs4 import BeautifulSoup as BS

URL = 'https://sadovod-opt.com/'

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data():
    html = get_html(URL)
    soup = BS(html.text, "html.parser")
    items = soup.find_all("div", class_="list-item")
    clothes = []
    for item in items:
        clothes.append({
            "title": item.find('div', class_="item-info").find('a').getText(),
            "link": URL + item.find('div', class_="item-info").find('a').get('href'),
            "info": item.find('div', class_="item-info").find('p').getText(),
        })
    return clothes




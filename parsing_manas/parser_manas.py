from http.client import responses

import requests
from bs4 import BeautifulSoup as BS4
from urllib3 import request

URL = 'https://manascinema.com'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

#start
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#get data
def get_data(html):
    bs = BS4(html, 'html.parser')
    items = bs.find_all('div', class_='schedule-block')
    manas_list = []
    for item in items:
        title = item.find('div', class_='creation-details').get_text(strip=True)
        image = URL + item.find('div', class_='creation-wrapper').find('img ').get('src')
        genre = item.find('div', class_='creation-genre').get_text(strip=True)
        scheldule = item.find('div', class_='creation-schedule')
        manas_list.append({
            'title': title, 'image': image,"genre": genre, "scheldule": scheldule
        })
    return manas_list

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        manas_list2 = []
        for page in range(1,2):
            response = get_html("https://manascinema.com/schedule", params={'page': page})
            manas_list2.extend(get_data(response.text))
        return manas_list2
    else:
        raise Exception("Parsing failed")


# print(parsing())










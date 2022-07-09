import requests
from bs4 import BeautifulSoup
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3770.100 Safari/537.36',
           'accept': '*/*'}

# url = 'https://news.rambler.ru/world/48353257-abramovich-ne-popal-pod-sanktsii-ssha-po-prosbe-zelenskogo/'
# url = 'https://edition.cnn.com/style/article/stan-t-rex-abu-dhabi-museum-scn/index.html'
# url = 'https://www.avito.ru/moskva/bytovaya_tehnika/holodilnik_liebherr_cp_40560_2388353239'
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
# url = 'https://www.gismeteo.ru/'

response = requests.get(url, headers=HEADERS, params=None)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.find('a', href_='/'))
# print(soup)
# items = soup.find('div', class_='col-md-8')
# print(items.find('a').get_text())
# items = soup.find('div', class_='col-md-4')
# print(items.find('a').get_text())
# name = soup.find('h1', class_='_34SJ8')
# items = soup.find_all('div', class_='l2dv- _2-nxy')
# abc = []
# for i in items:
#     abc.append(i.find('p').get_text())
# print(abc)
# print(items)
# print(name.get_text())

# https://edition.cnn.com/style/article/stan-t-rex-abu-dhabi-museum-scn/index.html
# спарсить заголовок и текст
# name = soup.find('h1', class_='PageHead__title')
# item = soup.find('div', class_='Paragraph__component BasicArticle__paragraph BasicArticle__pad Paragraph__isDropCap')
# items = soup.find_all('div', class_='Paragraph__component BasicArticle__paragraph BasicArticle__pad')
# print(name.get_text())
# print(item.get_text())
# for i in items:
#     text = i.find('a')
#     print(i.get_text())

# name = soup.find('h1', class_='title-info-title')
# print(name.get_text())
# price = soup.find('span', class_='js-item-price')
# print(price.get_text())
# name_owner = soup.find('div', class_='seller-info-name js-seller-info-name').find('a').get_text()
# print(name_owner)
# print(f'Название товара: {name.get_text()}\n цена: {price.get_text()}Р\n продавец: {name_owner}')
# a = name_owner.find('a')
# for i in name_owner:
#     a = i.find('a')
#     print(i.get_text())

# name_city = soup.find('a', class_='city-link link')
# print(name_city.get_text())
# weather = soup.find('span', class_='unit unit_temperature_c')
# print(weather.get_text())
# print(soup)


# https://openweathermap.org/
# http://www.cbr.ru/scripts/XML_daily.asp
# разобраться с сайтом ЦБРФ, попробовать что либо вывести

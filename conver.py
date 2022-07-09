import requests
from bs4 import BeautifulSoup


class Converter:
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/75.0.3770.100 Safari/537.36',
               'accept': '*/*'}

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def convert(self):
        response = requests.get(self.url, headers=self.HEADERS, params=None)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find('valcurs')
        valute_dict = {}
        for i in items:
            charcode = i.find('name')
            value = i.find('value')
            nominal = i.find('nominal')
            valute_dict[charcode.get_text()] = float(value.get_text().replace(',', "."))/float(nominal.get_text().replace(',', "."))
        return valute_dict
# id_find = items.find('charcode')
# print(id_find)
# print(soup)

# распарсить цбрф по айди

# почитать первые три номральные формы, про связи: один к одному, один ко многим, многие ко многим,
# про связи между таблицами(внешний ключ->первичный ключ)
# почитать про добавление значений в таблицы
# почитать про выборка SELECT, условия WHERE, COUNT MAX MIN - функции sql, GROUP BY DESC ASC
# добавить в таблицу grades оценки
# почитать про CURRENT_TIMESTAMP, SUBSTR +
# Найдите количество учеников в базе данных. Выведите искомое значение в столбец с
# именем total_students +
# Найдите среднюю успеваемости ученика по потокам с идентификатором
# равным 2
# попробовать SELECT student_id, AVG(grade) FROM grades GROUP BY student_id; + сказать, почему так получилось
# вывести месяц и год из CURRENT_TIMESTAMP +
# Покажите даты начала двух последних по времени потоков пример(SELECT DISTINCT(substr(started_at,1,4)) FROM training_groups;)
# DISTINCT - получение уникальных значений
# найдите идентификаторы (ниже)
# учеников, у которых средняя успеваемость по всем потокам меньше 4.8
# почитать https://unetway.com/tutorial/sqlite-operator-distinct + https://unetway.com/tutorial/sqlite-operator-having +
# https://unetway.com/tutorial/sqlite-syntax-alias + https://unetway.com/tutorial/sqlite-operator-limit +
# https://unetway.com/tutorial/sqlite-date-time + https://unetway.com/tutorial/sqlite-functions
# Найдите потоки, количество учеников в которых больше или равно 40. В отчет выведите
# номер потока, название курса и количество учеников.
# прочитать книгу грокаем алгоритмы

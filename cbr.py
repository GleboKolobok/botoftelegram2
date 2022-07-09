from collections import OrderedDict
import collections

houses_dict = {"Ленина 21": 40, 'Школьная 8': 30, "Садовая 12": 29, "Лесная 5": 70}
# apartment = houses_dict.get('Школьная 8')
# print(apartment)
# houses_dict['Есенина 1'] = 17
# houses_dict['Школьная 8'] = 45
# print(houses_dict)
# del houses_dict['Ленина 21']
# print(houses_dict)
# if 'Ленина 21' in houses_dict:
#     print('Да, такой ключ есть')
# else:
#     print('Такого ключа нет')
# print(len(houses_dict))
# for key in sorted(houses_dict):
#     print(key)
# for key, value in sorted(houses_dict.items(), key=lambda x: x[1]):
#     print(value)


# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением. Предполагается,
# что элементы списка будут соответствовать правилам задания ключей в словарях.

# abc = ['apple', 'pear']
#
#
# def to_dict(lst):
#     list = {}
#     for i in lst:
#         print(i)
#         list.update({i: i})
#     return list
#
#
# print(to_dict(abc))

# numbers = '8760231459'
# abc = {}
# for i in numbers:
#     i = int(i)
#     abc.update({i: len(numbers)})
#     print(abc)
#
#
# a = {'значение': 13}
# print(a.get('значение'))


# a = tuple() С помощью встроенной функции tuple()
# a = () С помощью литерала кортежа

# words = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1, 'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3,
#          'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10}
#
# summa = 0
# stroka = 'edcf'
# for i in stroka:
#     a = words.get(i)
#     summa += a
#
# print(summa)

# peoples = {'Ваня': 3, "Маша": 11, "Миша": 2, "Максим": 12}
# for key in peoples:
#     if peoples.get(key) >= 10:
#         print(key)

# new_dict = OrderedDict({'паша': 19, "маша": 10, "артем": 13, "илья": 15, "арсений": 16})
# first_item = list(new_dict.items())[0]
# second_item = list(new_dict.items())[1]
# last_item = list(new_dict.items())[-1]
# new_dict.move_to_end(first_item[0])
# new_dict.move_to_end(last_item[0], False)
# del new_dict[second_item[0]]
# new_dict['ваня'] = 11
# print(new_dict)
# for i in range(2):
#     last_item = list(new_dict.items())[-1]
#     new_dict.move_to_end(last_item[0], False)
# print(new_dict)
# for i in range(4):
#     last_item = list(new_dict.items())[-1]
#     new_dict.move_to_end(last_item[0], False)
# print(new_dict)


c = collections.Counter()
# for i in ['банан', "яблоко", "банан", "апельсин"]:
#     c[i] += 1
# print(c)

# for i in '':
#     c[i] += 1
# print(c.most_common())
# print(list(c.elements()))

# def_dict = collections.defaultdict(list)
# for i in range(5):
#     def_dict[i].append(i)
# print(def_dict)


# https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

# почитать про кортежи, множества, словари, списки

# https://docs-python.ru/standart-library/modul-collections-python/klass-ordereddict-modulja-collections/

# перевернуть словарь

# почитать про collections.namedtuple()

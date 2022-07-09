# class Phone:
#     def __init__(self, number, model, weight):
#         self.number = number
#         self.model = model
#         self.weight = weight
#
#     def receive_call(self, name):
#         print(f'Звонит {name}')
#
#     def get_number(self):
#         return self.number
#
#     def send_message(self, number1, number2):
#         print(number1)
#         print(number2)
#
#
# a = Phone(1, 2, 3)
# b = Phone(4, 5, 6)
# c = Phone(7, 8, 9)
# print(a.number)
# print(b.model)
# print(c.weight)
# a.receive_call('Ваня')
# print(b.get_number())
# c.send_message(a.number, b.number)


# class Nikola:
#     def __init__(self, age):
#         self.name = 'Николай'
#         self.age = age
#
#     def check_name(self, name):
#         if name == self.name:
#             return name
#         else:
#             print(f'Мое имя не {name}, а {self.name}')
#
#
# user = Nikola(13)
# user.check_name('Максим')


# class Static:
#     i = 0
#     @staticmethod
#     def staticmethod():
#         i = 0
#         i += 1
#         print(i)
#
#
# Static.staticmethod()
# obj = Static()
# obj.staticmethod()
#
#
# class Class:
#     @classmethod
#     def classmethod(cls):
#         i = 0
#         i += 2
#         print(i)
#
#
# Class.classmethod()
# ob = Class()
# ob.classmethod()


# obj = object()


# class Animal:
#     def run(self):
#         print('Животное бежит')
#
#
# class Cat(Animal):
#     def run(self):
#         print('Кот бежит')
#
#
# class Dog(Animal):
#     # def run(self):
#         # print('Собака бежит')
#     pass
#
#
# animal = Animal()
# cat = Cat()
# dog = Dog()
# animals = [animal, cat, dog]
# for i in animals:
#     i.run()


# class Auto:
#     def __init__(self, speed, gasoline_consumption, earmarking):
#         self.speed = speed
#         self.gasoline_consumption = gasoline_consumption
#         self.earmarking = earmarking
#
#
# class Legk(Auto):
#     def __init__(self, speed, gasoline_consumption, earmarking, mark):
#         super.__init__(speed, gasoline_consumption, earmarking)
#         self.mark = mark
#
#     def print_mark(self):
#         print(self.mark)
#
#
# class Spec(Auto):
#     def
#
#
# class Help(Spec):
#     pass
#
#
# class Police(Spec):
#     pass
#
#
# class Burn(Spec):
#     pass
#
#
# class Gruz(Auto):
#     pass


class Phone:
    def __init__(self):
        self.phone_book = {}

    def add_people(self, name, number):
        self.phone_book[name] = number

    def remove_people(self, name):
        del self.phone_book[name]

    def remove_number(self, number):
        for k, v in self.phone_book:
            if v == number:
                del self.phone_book[k]

    def search_people(self, name):
        for i in self.phone_book:
            if name == i:
                return i

    def search_number(self, number):
        for i in self.phone_book:
            if number == i:
                return i

    def print_book(self):
        print(self.phone_book)


owner = Phone()
owner.add_people('олег', '12345')
# owner.remove_number('12345')
owner.print_book()


# дз: почитать https://proglib.io/p/python-oop, сделать акцент на : Жизненный цикл объекта, сборщик мусора(как он удаляет объекты),
# метаклассы


# написать класс телефонной книги, /добавление человека в телефонной книге, Удаление
# человека из телефонной книги,Добавление номера,Удаление номера, поиск людей по телефону, поиск телефона по людям

# https://github.com/vadim8901/PhoneBook1/blob/master/src/main/java/PhoneBook.java

# почитать https://openweathermap.org/current, https://openweathermap.org/api/geocoding-api


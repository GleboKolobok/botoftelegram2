import telebot
import config
import otherrealisation

bot = telebot.TeleBot(config.TOKEN)


def add(message):
    number_one, number_two = get_numbers(message.text)
    bot.send_message(message.chat.id, f'Результат работы: {int(number_one)+int(number_two)}')


def minus(message):
    number_one, number_two = get_numbers(message.text)
    bot.send_message(message.chat.id, f'Результат работы: {int(number_one)-int(number_two)}')


def multiply(message):
    number_one, number_two = get_numbers(message.text)
    bot.send_message(message.chat.id, f'Результат работы: {int(number_one) * int(number_two)}')


def division(message):
    number_one, number_two = get_numbers(message.text)
    bot.send_message(message.chat.id, f'Результат работы: {int(number_one) / int(number_two)}')


def get_numbers(text):
    result = otherrealisation.parsing(text)
    return result[0], result[1]

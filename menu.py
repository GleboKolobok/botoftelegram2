import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)


def main_menu():
    markup = types.InlineKeyboardMarkup()
    key_conv = types.InlineKeyboardButton(text='Курсы валют', callback_data='yes')
    key_calc = types.InlineKeyboardButton(text='Калькулятор', callback_data='no')
    key_weather = types.InlineKeyboardButton(text='Погода', callback_data='maybe')
    markup.add(key_conv, key_calc, key_weather)
    return markup


def calc():
    markup = types.InlineKeyboardMarkup()
    key_plus = types.InlineKeyboardButton(text='Сложить', callback_data='1')
    key_minus = types.InlineKeyboardButton(text='Вычесть', callback_data='2')
    key_multiply = types.InlineKeyboardButton(text='Умножить', callback_data='3')
    key_division = types.InlineKeyboardButton(text='Разделить', callback_data='4')
    markup.add(key_plus, key_minus, key_multiply, key_division)
    return markup


def weather():
    markup = types.InlineKeyboardMarkup()
    moscow = types.InlineKeyboardButton(text='Москва', callback_data='moscow')
    new_york = types.InlineKeyboardButton(text='Нью Йорк', callback_data='new_york')
    london = types.InlineKeyboardButton(text='Лондон', callback_data='london')
    paris = types.InlineKeyboardButton(text='Париж', callback_data='paris')
    warshaw = types.InlineKeyboardButton(text='Варшава', callback_data='warshaw')
    berlin = types.InlineKeyboardButton(text='Берлин', callback_data='berlin')
    markup.add(moscow, new_york, london, paris, warshaw, berlin)
    return markup

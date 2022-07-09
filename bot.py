import calculator
import config
import telebot
from telebot import types
import menu
import weather
import conver


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Привет, добро пожаловать!', reply_markup=menu.main_menu())


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, 'Меню команд:\n/start\n/info')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.from_user.id, 'Краткая информация о боте:\nБот умеет переводить валюты, считать и '
                                           'узнавать погоду')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.from_user.id, 'Извини, я не понимаю тебя, напиши /help')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    weath = weather.Weather()
    conv = conver.Converter()
    if call.data == 'no':
        bot.send_message(call.message.chat.id, 'Меню калькулятора:', reply_markup=menu.calc())
    elif call.data == '1':
        bot.send_message(call.message.chat.id, 'Введи два числа в формате: число,число')
        bot.register_next_step_handler(call.message, calculator.add)
    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'Введи два числа в формате: число,число')
        bot.register_next_step_handler(call.message, calculator.minus)
    elif call.data == '3':
        bot.send_message(call.message.chat.id, 'Введи два числа в формате : число,число')
        bot.register_next_step_handler(call.message, calculator.multiply)
    elif call.data == '4':
        bot.send_message(call.message.chat.id, 'Введи два числа в формате: число,число')
        bot.register_next_step_handler(call.message, calculator.division)
    elif call.data == 'yes':
        value_dict = conv.convert()
        text = ''
        text += 'Курс валют:\n'
        for element in value_dict:
            text += f'Валюта: {element}, курс: {value_dict[element]}\n'
        bot.send_message(call.message.chat.id, text)
    elif call.data == 'maybe':
        bot.send_message(call.message.chat.id, 'Меню погоды:', reply_markup=menu.weather())
    elif call.data == 'moscow':
        result = weath.set_weather_city([55.7522, 37.6156])
        bot.send_message(call.message.chat.id, f'В городе Москва\nПогода: {result[1]}\nТемпература: {round(result[0])}')
    elif call.data == 'new_york':
        result = weath.set_weather_city([40.7143, -74.006])
        bot.send_message(call.message.chat.id, f'В городе Нью Йорк\nПогода: {result[1]}\nТемпература: {round(result[0])}')
    elif call.data == 'london':
        result = weath.set_weather_city([51.5085, -0.12574])
        bot.send_message(call.message.chat.id, f'В городе Лондон\nПогода: {result[1]}\nТемпература: {round(result[0])}')
    elif call.data == 'paris':
        result = weath.set_weather_city([48.8534, 2.3488])
        bot.send_message(call.message.chat.id, f'В городе Париж\nПогода: {result[1]}\nТемпература: {round(result[0])}')
    elif call.data == 'warshaw':
        result = weath.set_weather_city([52.2298, 21.0118])
        bot.send_message(call.message.chat.id, f'В городе Варшава\nПогода: {result[1]}\nТемпература: {round(result[0])}')
    elif call.data == 'berlin':
        result = weath.set_weather_city([52.5244, 13.4105])
        bot.send_message(call.message.chat.id, f'В городе Берлин\nПогода: {result[1]}\nТемпература: {round(result[0])}')


bot.polling(none_stop=True, interval=0)


from telebot import TeleBot, types
from telebot.types import Message, ReplyKeyboardRemove
from pprint import pprint
from buttons import *
from datetime import datetime
import requests

bot = TeleBot("6878848160:AAH6QkZs5ecP8gxg7Ym9IxZcpj3uUdVYpns")


def weather(city_name):
    parametres = {
        "q": city_name,
        "appid": "b01e7608c07f15c54ff9d9b64d478705",
        "units": "metric"
    }

    res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parametres).json()
    pprint(res)
    temp = res['main']['temp']
    city = res['name']
    description = res['weather'][0]['description']
    wind = res['wind']['speed']
    sunrise = datetime.utcfromtimestamp(res['sys']['sunrise'] + res['timezone']).strftime("%Y.%d.%m  %H:%M:%S")
    sunset = datetime.utcfromtimestamp(res['sys']['sunset'] + res['timezone'])
    info = f"""🏙 {city} shaxrida
⛅️ ob havo min va max {temp} °C
💨 shamol {wind}
☀️ quyosh chiqishi {sunrise}
🌇 quyosh botishi {sunset}
description {description}"""
    return info


def weather_from_location(latitude, longitude):
    parametres = {
        "lat": latitude,
        "lon": longitude,
        "appid": "b01e7608c07f15c54ff9d9b64d478705",
        "units": "metric"
    }

    res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parametres).json()
    pprint(res)
    temp = res['main']['temp']
    city = res['name']
    description = res['weather'][0]['description']
    wind = res['wind']['speed']
    sunrise = datetime.utcfromtimestamp(res['sys']['sunrise'] + res['timezone']).strftime("%Y.%d.%m  %H:%M:%S")
    sunset = datetime.utcfromtimestamp(res['sys']['sunset'] + res['timezone'])
    info = f"""🏙 {city} shaxrida
⛅️ ob havo min va max {temp} °C
💨 shamol {wind}
☀️ quyosh chiqishi {sunrise}
🌇 quyosh botishi {sunset}
description {description}"""
    return info


def start_bot_polling():
    @bot.message_handler(commands=["start"])
    def start(message: Message):
        bot.send_message(message.chat.id, "Joriy ob havo botiga hush kelibsz! ", reply_markup=main_menu())

    @bot.message_handler(func=lambda message: message.text == "Shaharlar bo'yicha")
    def reaction_to_weather(message: Message):
        bot.send_message(message.chat.id, "Shahar nomini kiriting!", reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id, "Mamlakatni tanlang:", reply_markup=countrys())

    @bot.message_handler(func=lambda message: message.text == "O'zbekiston")
    def check_country_uz(message: Message):
        bot.send_message(message.chat.id, "shahardan birini tanlang!", reply_markup=uz_citys())

    @bot.message_handler(func=lambda message: message.text == "USA")
    def check_country_uz(message: Message):
        bot.send_message(message.chat.id, "Bunday ro'yxat mavjud emas", reply_markup=countrys())

    @bot.message_handler(content_types=["location"])
    def location(message: Message):
        lat = message.location.latitude
        lon = message.location.longitude
        res = weather_from_location(lat, lon)
        bot.send_message(message.chat.id, res)

    @bot.message_handler(content_types=["text"])
    def weather2(message: Message):
        if message.text == "main menu":
            bot.send_message(message.chat.id, "Main menuga qaytildi", reply_markup=main_menu())
        else:
            try:
                res = weather(message.text)
                bot.send_message(message.chat.id, res)
            except:
                bot.send_message(message.chat.id, f" {message.text} Bunday shahar topoilmadi")

    bot.infinity_polling()





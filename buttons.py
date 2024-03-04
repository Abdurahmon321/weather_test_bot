from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = KeyboardButton("Shaharlar bo'yicha")
    button2 = KeyboardButton("Joylashgan joyi bo'yicha", request_location=True)
    markup.add(button1, button2)
    return markup


def countrys():
    markup1 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    country = KeyboardButton("O'zbekiston")
    country2 = KeyboardButton("USA")
    markup1.add(country, country2)
    return markup1


def uz_citys():
    markup3 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    city1 = KeyboardButton("Fergana")
    city2 = KeyboardButton("Namangan")
    city3 = KeyboardButton("Andijon")
    city4 = KeyboardButton("Toshkent")
    city5 = KeyboardButton("Navoiy")
    city6 = KeyboardButton("Jizzax")
    city7 = KeyboardButton("Samarqand")
    city8 = KeyboardButton("Xorazm")
    city9 = KeyboardButton("Buxoro")
    city10 = KeyboardButton("Qashqadaryo")
    city11 = KeyboardButton("Sirdaryo")
    city12 = KeyboardButton("Surxandaryo")
    button3 = KeyboardButton("main menu")
    markup3.add(city1, city11, city12, city10, city5, city6, city7, city8, city9, city2, city3, city4, button3)
    return markup3

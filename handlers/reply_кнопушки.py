import random
import telebot
from handlers.paths import a
from init import bot


@bot.message_handler(commands=["motivate_me"])
def reply_buttons(message: telebot.types.Message, ):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    markup.add(telebot.types.KeyboardButton("Цитата дня"))
    markup.add(telebot.types.KeyboardButton("Книга"),
               telebot.types.KeyboardButton("Картинка для вдохновения")
               )
    markup.add(telebot.types.KeyboardButton("Трек-мотивация"),
               telebot.types.KeyboardButton("Фильм/сериал")
               )
    bot.reply_to(message, "Что выберешь сегодня?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Цитата дня')
def get_citatio(message: telebot.types.Message):
    with open("citations.txt", "r", encoding="utf-8") as file:
        cites = file.read().split("\n")
    cite = random.choice(cites)
    bot.send_message(message.chat.id, cite)


@bot.message_handler(func=lambda message: message.text == "Книга")
def get_book(message: telebot.types.Message):
    with open("books.txt", "r", encoding="utf-8") as file:
        books = file.read().split("\n")
    book = random.choice(books)
    bot.send_message(message.chat.id, book, parse_mode="MarkdownV2")


@bot.message_handler(func=lambda message: message.text == "Трек-мотивация")
def get_track(message: telebot.types.Message):
    with open("tracks.txt", "r", encoding="utf-8") as file:
        tracks = file.read().split("\n")
    track = random.choice(tracks)
    bot.send_message(message.chat.id, track, parse_mode="MarkdownV2")


@bot.message_handler(func=lambda message: message.text == "Фильм/сериал")
def get_film(message: telebot.types.Message):
    with open("films.txt", "r", encoding="utf-8") as file:
        films = file.read().split("\n")
    film = random.choice(films)
    bot.send_message(message.chat.id, film, parse_mode="Markdownv2")


@bot.message_handler(func=lambda message: message.text == "Картинка для вдохновения")
def get_picture(message: telebot.types.Message):
    picture_path = random.choice(a)
    with open(picture_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

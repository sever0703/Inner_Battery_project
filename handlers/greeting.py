import telebot
from funcs.datetime_func import get_welcome
from init import bot


@bot.message_handler(commands=["start", "help"])
def greeting(message: telebot.types.Message):
    text = f"{get_welcome().replace("!", "\!").replace(")", "\)").replace("_", "\_")}"
    bot.send_message(message.chat.id, text, parse_mode="MarkdownV2")

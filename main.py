import telebot
from telebot import types
import Controller

bot = telebot.TeleBot('5590063865:AAGKGDAL1qM2DLgtDfmx60gazVUsBNHyCCw')

with open ('rule.txt', 'r', encoding='utf-8') as file:
    rule = file.read()

@bot.message_handler(commands=['start'])
def start(message):
    text = '<b>Для начала игры введите слово "игра"</b>'
    bot.send_message(message.chat.id, text, parse_mode='html')


@bot.message_handler(content_types=['text'])
def game(message):
    check_game = Controller.game_control(message.from_user.first_name, message.from_user.id, message.text.lower())
    if message.text.lower() == 'игра' and check_game == 'игра начата':
        text = 'Игра уже начата, жду Вашего хода'
        bot.send_message(message.chat.id, text, parse_mode='html')
    elif message.text.lower() == 'игра' and (check_game == 'первая игра' or check_game == 'новая игра'):
        text = rule
        bot.send_message(message.chat.id, text, parse_mode='html')
    elif message.text.isdigit() and (check_game == 'игра начата' or check_game == 'новая игра'):
            text = Controller.step_game(int(message.text), message.from_user.id)
            bot.send_message(message.chat.id, text, parse_mode='html')
    elif message.text.lower() == 'сброс':
        Controller.clear_game(message.from_user.id)
        text = '<b>Для начала игры введите слово "игра"</b>'
        bot.send_message(message.chat.id, text, parse_mode='html')
    else:
        text = 'Для начала игры введите слово "игра".\nДля того чтобы сделать ход введите количество конфет.\nДля сброса игры введите слово "сброс"'
        bot.send_message(message.chat.id, text, parse_mode='html')
bot.polling(none_stop=True)






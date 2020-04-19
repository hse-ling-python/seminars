# python 3.7.1

import telebot  # импортируем модуль pyTelegramBotAPI
import conf     # импортируем наш секретный токен
import create_markov_model
import requests


telebot.apihelper.proxy = conf.PROXY  # задаем прокси
bot = telebot.TeleBot(conf.TOKEN)  # создаем экземпляр бота


# этот обработчик запускает функцию send_welcome,
# когда пользователь отправляет команды /start или /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте! Я умею отвечать пословицами и присылать фотки собак /dog")


# этот обработчик присылают рандомные фотки собак
@bot.message_handler(commands=['dog'])
def bop(message):
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    bot.send_photo(chat_id=message.chat.id, photo=url)


# этот обработчик реагирует на любое сообщение
@bot.message_handler(func=lambda m: True)
def send_len(message):
    bot.send_message(message.chat.id, create_markov_model.m.make_short_sentence(100))
    #bot.send_message(message.chat.id, 'В вашем сообщении {} символов.'.format(len(message.text)))


if __name__ == '__main__':
    bot.polling(none_stop=True)

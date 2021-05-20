import uuid
import os
import random

import telebot

import text2emotion as te
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment

import conf


r = sr.Recognizer()
bot = telebot.TeleBot(conf.TOKEN)
citations = open("citations.txt").readlines()

stickers = {
    'Angry': "CAACAgIAAxkBAAEBURNgpkd8dl6RuqzpNdgu94AOEkS9qgAC9gIAArrAlQX_E5eYMPePyR8E",
    'Fear': "CAACAgIAAxkBAAEBUR9gpkiHGe1Gviv7aDJLX4F949gz_wACFQAD6dgTKB_wcbmZuMxBHwQ",
    'Happy': "CAACAgIAAxkBAAEBUSJgpkipoqAQEjje5qU4nECW7V_RqQACegEAAhZCawqYRZuYnxC0lx8E",
    'Sad': "CAACAgIAAxkBAAEBURlgpkg4sRUk-EJiOR976KQYXor_hwACrwADFkJrCjbMlkF58CJCHwQ",
    'Surprise': "CAACAgIAAxkBAAEBURZgpkgH6WCYCNOu0UPrB0oQWPYMvgACcxoAAtjY4QAB835omK7qbNYfBA"
}


@bot.message_handler(commands=['start', 'help'])
def help(message):
    user = message.chat.id
    bot.send_message(user, """
    Этот бот умеет делать 3 вещи:
    - /sayit : выдает цитату на английском и ее озвучивает
    - текст : на английском определяет эмоцию и отвечает стикером
    - войс на русском : распознает текст
    """)


@bot.message_handler(content_types=['voice'])
def text_recognition(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = uuid.uuid4().hex
    with open(f'{filename}.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)

    ogg_version = AudioSegment.from_ogg(f"{filename}.ogg")
    ogg_version.export(f"{filename}.wav", format="wav")

    user_audio_file = sr.AudioFile(f"{filename}.wav")
    with user_audio_file as source:
        user_audio = r.record(source)
    text = r.recognize_google(user_audio, language='ru')

    os.remove(f"{filename}.wav")
    os.remove(f"{filename}.ogg")

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["sayit"])
def say_it(message):
    text = random.choice(citations)
    filename = f"{uuid.uuid4().hex}.mp3"
    engine = pyttsx3.init(driverName="espeak")  # sapi5 on Widows
    # Linux/Mac:  sudo apt install espeak
    engine.setProperty('voice', 'en')
    engine.save_to_file(text, filename)
    engine.runAndWait()
    # time.sleep(1)
    bot.send_message(message.chat.id, text)
    with open(filename, "rb") as audio:
        bot.send_voice(message.chat.id, audio)
    os.remove(filename)


@bot.message_handler(content_types=['text'])
def echo(message):
    text = message.text
    emotions = te.get_emotion(text)
    emotion = max(emotions, key=emotions.get)
    bot.send_sticker(message.chat.id, stickers.get(emotion))


if __name__ == "__main__":
    bot.polling(none_stop=True)

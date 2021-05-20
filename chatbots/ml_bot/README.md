# Бот с использованием готовых моделей


## Требования
```
text2emotion
pyttsx3
speech_recognition
pydub
```

Для pyttsx3 нужно установить espeak, если у вас Mac / Linux

Linux
```
sudo apt install espeak
```
MacOS 
```
brew install espeak
```

Windows должен быть sapi5 по умолчанию


## Описание работы

### Распознавание эмоций в сообщениях

Библиотека **text2emotion** распознает эмоции: angry, happy, sad, fear, surprise.

Эта функция реагирует на текстовые сообщения. Функция get_emotion отдает словарь с вероятностями, бот выбирает максимальную и отвечает соответствующим стикером из словаря стикеров.

```
import text2emotion as te
emotions = te.get_emotion(text)
emotion = max(emotions, key=emotions.get)
```

### Распознавание речи

Библиотека speech_recognition позволяет использовать разные ресурсы для распознавания речи (speech to text). Например, Sphinx open-source speech recognition. Мы будет использовать Google для работы с русским языком. API бесплатное до некоторого предела, поэтому может.

Импортируем библиотеку и создаем объект, соержащий нужные методы.
```
import speech_recognition as sr
from pydub import AudioSegment

r = sr.Recognizer()
```
В обработчике сообщений аудио получает адрес файла и скачиваем специальной функцией.
```
file_info = bot.get_file(message.voice.file_id)
downloaded_file = bot.download_file(file_info.file_path)
```
Чтобы не пересекались файлы пользователей создаем временное имя файла - с помощью библиотеки uuid, которая генерирует ID вроде 6d32a89b6d4246da9d97237f291a828f. Считанный файл записываем как write binary. Формат голосовых - ogg. Его нужно перекодировать с помощью pydub. Считываем ogg файл и экспортируем в wav формате, который принимает парсер.
```
filename = uuid.uuid4().hex
with open(f'{filename}.ogg', 'wb') as new_file:
    new_file.write(downloaded_file)

ogg_version = AudioSegment.from_ogg(f"{filename}.ogg")
ogg_version.export(f"{filename}.wav", format="wav")
```
**возможно, что можно проще, но пока так**

Считываем обратно wav через распознаватель, обрабатываем через запись из файла и парсим с помощью google распознавателя с настройкой, что это русский язык.

```
user_audio_file = sr.AudioFile(f"{filename}.wav")
with user_audio_file as source:
    user_audio = r.record(source)
text = r.recognize_google(user_audio, language='ru')
```
Удаляем оба файла, чтобы они не засоряли диск, отправляет текст распознанный пользователю.
```
os.remove(f"{filename}.wav")
os.remove(f"{filename}.ogg")

bot.send_message(message.chat.id, text)
```


### Генерация речи

Генерация через библиотеку pyttsx3. Она использует дополнительные программы, поэтому нужно это проконтролировать. Здесь пример для Linux ("espeak").

1. Выбираем случайную цитату
2. Создаем имя для файла временного
3. Запускаем pyttsx3
4. Задаем настройку языка
5. Сохраняем в файл
6. Ждем обработку
7. Отправляем текст пословицы, а затем войс с результатом озвучки
8. Удаляем файл
```
text = random.choice(citations)
filename = f"{uuid.uuid4().hex}.mp3"

engine = pyttsx3.init(driverName="espeak")
engine.setProperty('voice', 'en')
engine.save_to_file(text, filename)
engine.runAndWait()

bot.send_message(message.chat.id, text)

with open(filename, "rb") as audio:
    bot.send_voice(message.chat.id, audio)

os.remove(filename)
```

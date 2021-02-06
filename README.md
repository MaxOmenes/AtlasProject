# Atlas #
========================

### Цели проекта: ###
---------------------
	Создание голосового помощника, с помощью которого можно будет просто искать информацию в сети интернет, управлять файлами на компьютере, а также управлять музыкой из Spotify

### Чем Атлас отличается от других голосовых помощников? ###
------------------------------------------------------------
 - Атлас отличается тем, что он может управлять системой и файлам, а не только работать с интернетом
 - Атлас создаётся с упором на людей с ограниченными возможностями 



##### Цели #####
    >>1. Yandex_recognition
    >>2. Логика распознования команд
    >>3. Spotify API
    >>4. Работа с файлами
    >>5. Поиск в интернете [Done]
    >>6. Привязать код к кнопке [Done]

##### Необходимые модули #####
    Pyttsx:
    pip install pyttsx3

    PyAudio:
    pip install pipwin
    pipwin install pyaudio

    SpeechRecognition:
    pip install SpeechRecognition

    FuzzyWuzzy:
    pip install fuzzywuzzy
---------------------------------------------------------
mic.py - для вывода списка микрофона, индекс микрофона вписывается в voice.recognizer


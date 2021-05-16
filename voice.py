import pyttsx3 as pyx
import speech_recognition as sr

#locale = "en-EN"
locale = "ru-RU"

def say(request):
    engine = pyx.init()
    engine.say(request)
    engine.runAndWait()

def recognizer():
    rec = sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:
            user_audio = rec.listen(source)
            query = rec.recognize_google(user_audio, language=locale).lower()
    except:
        say("Command not recognized")
    
    return query








 
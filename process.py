from voice import say, recognizer
import webbrowser
import os
import time
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

#phrases library
phrases = {
    "name": ('Atlas','assistant'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds": {
        "time_cmd": ('time','whats the time'),
        "spotify_cmd": ('lets listen to music'),
        "chrome_cmd": ('find')
    }
}


def chrome(request):
   webbrowser.open_new_tab("https://yandex.ru/search/?text=" + request)


def callback():
    try:
        voice = recognizer()
        chrome(voice)
        
        #Need to rewrite
        '''if voice.startswith(phrases["name"]):
            cmd = voice
            for x in phrases['name']:
                cmd = cmd.replace(x, "").strip()
            for x in phrases['tbr']:
                cmd = cmd.replace(x, "").strip()
            cmd = recognize_cmd(cmd)
            #execute_cmd(cmd['cmd'])'''
           
 
    except:
        say("Voice not recognized, please repeat")
        
        #Not used     
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in phrases['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC


#Need to rewrite
"""
def execute_cmd(cmd):
    if cmd == 'time_cmd':
        now = datetime.datetime.now()
        say("Now" + str(now.hour) + str(now.minute))
    elif cmd == 'chrome_cmd':
        chrome(cmd)
    else:
         say('Command not recognized, try again!')
"""

#callback()



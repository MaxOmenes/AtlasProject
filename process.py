from voice import say, recognizer
import webbrowser
import os
import time
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import subprocess as sp
import re
import win32api
from colorama import Back, Fore


#cmd_library library
cmd_library = {
    "name": ('Atlas','assistant'),
    "tbr": ('say','tell','tell me'),
    "cmds": {
        "time_cmd": ('time','whats the time'),
        "spotify_cmd": ('lets listen to music'),
        "chrome_cmd": ('find', 'search')
    }
}

#apps
def chrome(request):
    if '.' in request:
        webbrowser.open_new_tab("https://"+request)
    else:
        webbrowser.open_new_tab("https://yandex.ru/search/?text=" + request)

def notepad(text):
    f = open('note.txt', 'w')
    f.write(text + "\n")
    f.close()

##########################_FileFinder_libs_##############################
def find_file(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                File_Path = os.path.join(root, f)
                break # if you want to find only one
    return File_Path

def find_file_in_all_drives(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        x = find_file( drive, rex )
    return x

def hope(request):
    request = request.replace('dog', 'doc')
    request = request.replace('com', 'doc')
    request = request.replace('дог', 'doc')
    request = request.replace('ru ', '')
    request = request.replace(' dat ', '.')
    request = request.replace(' точка ','.')
    request = request.replace(' дочка ','.')
    request = request.replace(' dad ','.')
    request = request.replace(' date ', '.')
    request = request.replace(' data', '.')
    
    return request
#########################################################################

def FileFinder(file_name):
    file_name = hope(file_name)
    print(Back.YELLOW + Fore.BLACK+ "[log] Recognized", file_name)
    try:
        Path = find_file_in_all_drives(file_name)
        os.startfile(Path)
    except:
        say("File not found")
def StartApp(name):
    print(Back.GREEN + Fore.BLACK+ "[log] Recognized " + name)
    try:
        os.startfile(r"C:\Users\ukhin\Desktop\\"+ name)
    except:
        try:    
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\"+ name)
        except:
            os.startfile(r"C:\Users\ukhin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\\"+ name)
    


#voice assistant base
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in cmd_library['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC


def execute_cmd(cmd):
    if 'время' in cmd:                                  #Time Mashine
        now = datetime.datetime.now()
        say("Now" + str(now.hour) + str(now.minute))
    elif 'найди' in cmd:                                #Internet Browsing
        cmd = cmd.replace('найди', '') 
        chrome(cmd)
    elif 'открой файл' in cmd:                          #FileFinder (Need to rewrite!)
        cmd = cmd.replace('открой файл', '') 
        FileFinder(cmd)
    elif 'запиши заметку' in cmd:                       #Notepad
        say("I'm listening")
        UserText = ''
        while UserText != "конец":
            UserText += recognizer()
            notepad(UserText)
        sp.Popen(['notepad', "note.txt"])
    elif 'запусти' in cmd:                              #StartApp
        cmd = cmd.replace('запусти ', '')
        try:
            StartApp(cmd)
        except:
            say("Program name not recognized")
    else:                                               #Internet Browsing
        chrome(cmd)


def callback():
        voice = recognizer()
        #Need to rewrite
        execute_cmd(voice)



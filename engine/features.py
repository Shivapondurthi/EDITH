from playsound import playsound
import eel
from hugchat import hugchat
import webbrowser
import pyttsx3
import sqlite3
import struct
import os
import subprocess
import pyaudio
import pyautogui
import wikipedia

import time
from engine.config import ASSISTANT_NAME
from engine.command import speak

#starting sound of EDITH

@eel.expose
def play_sound():
    sound_file="www\\bot_files\\audio_file\\www_assets_audio_start_sound (1).mp3"
    playsound(sound_file)

play_sound()

# play_sound

def speak1(text):
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')
     engine.setProperty('voice', voices[1].id)
     engine.setProperty('rate', 165)  # Lower values make speech slower
     engine.say(text)
     engine.runAndWait()    

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("opening"+query)
        os.system("start"+query)
    else:
        speak1("please say the name of the app")




def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    
    
    return response







    # app_name = query.strip()

    # if app_name != "":

    #     try:
    #         cursor.execute(
    #             'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
    #         results = cursor.fetchall()

    #         if len(results) != 0:
    #             speak("Opening "+query)
    #             os.startfile(results[0][0])

    #         elif len(results) == 0: 
    #             cursor.execute(
    #             'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
    #             results = cursor.fetchall()
                
    #             if len(results) != 0:
    #                 speak("Opening "+query)
    #                 webbrowser.open(results[0][0])

    #             else:
    #                 speak("Opening "+query)
    #                 try:
    #                     os.system('start '+query)
    #                 except:
    #                     speak("not found")
    #     except:
    #         speak("some thing went wrong")

       

# def PlayYoutube(query):
#     search_term = extract_yt_term(query)
#     speak("Playing "+search_term+" on YouTube")
#     kit.playonyt(search_term)


# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
       
#         # pre trained keywords    
#         porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword)

#             # checking first keyword detetcted for not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key win+j
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("j")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()


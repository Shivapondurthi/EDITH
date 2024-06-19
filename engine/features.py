from playsound import playsound
import eel
from hugchat import hugchat
import webbrowser
import pyttsx3

import os

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
    response =  chatbot.chat(user_input+"in 500 characters")
    
    
    return response








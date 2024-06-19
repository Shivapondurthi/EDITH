import eel
import pyttsx3
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import time
import pyautogui
import os
import subprocess


#Speak function using pyttsx3
def speak(text):
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')
     engine.setProperty('voice', voices[1].id)
     engine.setProperty('rate', 165)  # Lower values make speech slower
     engine.say(text)
     engine.runAndWait()
     


#speak function using uk accent
# speak command
# def speak(command):
#     gtts = gTTS(command, lang='en', tld='com.in')
#     gtts.save('hello1.mp3')
#     playsound('hello1.mp3')



#speech_recognizing 

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as Source:
        speak("Hello, I am coral....")
        print("listening....")
        eel.DisplayMessage("Listening....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(Source)

        audio=r.listen(Source,10,6)

    try:
        print("Recogining...")
        eel.DisplayMessage("Recogizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}")
        
        eel.DisplayMessage(query)
        

        
    except Exception as e:
        return query.lower()
    
    return query.lower()

@eel.expose
def allCommands():
        query1=takecommand()
        print(query1)

        if "open youtube" in query1:
            eel.DisplayMessage("Here you go to Youtube")
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif "google" in query1:
            eel.DisplayMessage("Here you go to Google")
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
        elif "open notepad" in query1:
            speak("here u go to notepad...")
            subprocess.Popen("notepad.exe")

        elif "screenshot" in query1:
            speak("ok takeing screenshot")
            im = pyautogui.screenshot()
            speak("imagename")
            saveimg="screenshot"
            extenion1=".jpg"
            im.save(saveimg+extenion1)
            speak("successfully taken scereenshot")

        elif "open microsoft word" in query1:
            speak("here u go to microsoft word...")
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(wordPath)

        elif "open calculator" in query1:
            speak("here u go to calculator...")
            subprocess.Popen("calc.exe") 
        
        elif "open clock" in query1:
            speak("opening clock...")
            subprocess.Popen("clock.exe")
        
             
        
        
        else:
             from engine.features import chatBot
             chat1=chatBot(query1)
             chat1=str(chat1)
             eel.DisplayMessage(chat1)
             print(chat1)
             speak(chat1)


        time.sleep(8)
        eel.showhood()


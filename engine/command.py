import eel
import pyttsx3
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import time


#Speak function using pyttsx3
def speak(text):
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')
     engine.setProperty('voice', voices[1].id)
     engine.setProperty('rate', 165)  # Lower values make speech slower
     engine.say(text)
     engine.runAndWait()
     

speak("hello")
#speak function using uk accent
# speak command
# def speak(command):
#     gtts = gTTS(command, lang='en', tld='com.in')
#     gtts.save('hello1.mp3')
#     playsound('hello1.mp3')



#speech_recognizing 
@eel.expose
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as Source:
        speak("Hello, I am Edith....")
        print("listening....")
        eel.DisplayMessage("Listening....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(Source)

        audio=r.listen(Source,10,10)

    try:
        print("Recogining...")
        eel.DisplayMessage("Recogizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}")
        speak(query)
        eel.DisplayMessage(query)
        time.sleep(5)
        eel.showhood()
    except Exception as e:
        return ""
    
    return query.lower()






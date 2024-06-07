import eel
import pyttsx3
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr


#Speak function using pyttsx3
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)  # Lower values make speech slower
    engine.say(text)
    engine.runAndWait()


#speak function using uk accent
#speak command
# def speak(command):
#     gtts = gTTS(command, lang='en', tld='com.in')
#     gtts.save('hello.mp3')
#     playsound('hello.mp3')



#speech_recognizing 
@eel.expose
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as Source:
        print("listening....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(Source)

        audio=r.listen(Source,10,10)

    try:
        print("Recogining...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}")
        speak(query)
        eel.DisplayMessage("hello")
    except Exception as e:
        return ""
    
    return query.lower()






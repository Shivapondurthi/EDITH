from playsound import playsound
import eel
from hugchat import hugchat
import webbrowser
import os
import subprocess
import wikipedia
from engine.command import speak
from engine.config import ASSISTANT_NAME
#starting sound of EDITH

@eel.expose
def play_sound():
    sound_file="www\\bot_files\\audio_file\\www_assets_audio_start_sound (1).mp3"
    playsound(sound_file)

play_sound()

# play_sound()

def senoritava():
    
    
    while True:
        query = takecommand().lower()
      
        if "open youtube" in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif "open code" in query:
            speak("here u go to pycharm.happy codeing...")
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2022.2.3.lnk" 
            os.startfile(codePath)

        elif "open microsoft word" in query:
            speak("here u go to microsoft word...")
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(wordPath)
        
        elif "open powerpoint" in query:
            speak("here u go to powerpoint...")
            powerpointPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(powerpointPath)

        elif "open microsoft excel" in query:
            speak("here u go to excel...")
            excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(excelPath)

        elif "open firefox" in query:
            speak("here u go to firefox...")
            firefoxPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk"
            os.startfile(firefoxPath)

        elif "open microsoft edge" in query:
            speak("here u go to microsoft edge...")
            edgePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            os.startfile(edgePath)

        elif "open powerpoint" in query:
            speak("here u go to powerpoint...")
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(codePath)

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("according to wikipidia....")
            print(results)
            speak(results)

        elif "open notepad" in query:
            speak("here u go to notepad...")
            subprocess.Popen("notepad.exe")
            
        elif "open calculator" in query:
            speak("here u go to calculator...")
            subprocess.Popen("calc.exe")

        elif "open notepad" in query:
            speak("opening notepad...")
            subprocess.Popen("notepad.exe")    
        
        elif "open calculator" in query:
            speak("opening calculator...")
            subprocess.Popen("calc.exe")
            
        elif "open paint" in query:
            speak("opening paint...")
            subprocess.Popen("paint.exe")
            

        elif "open clock" in query:
            speak("opening clock...")
            subprocess.Popen("clock.exe")
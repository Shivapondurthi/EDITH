import eel
import os


from engine.features import *
from engine.command import *


eel.init("www")
play_sound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html',mode=None,host="localhost",block=True) 

text=takecommand()
speak(text)

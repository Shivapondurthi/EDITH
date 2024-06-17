from playsound import playsound
import eel
#starting sound of EDITH

@eel.expose
def play_sound():
    sound_file="www\\bot_files\\audio_file\\www_assets_audio_start_sound (1).mp3"
    playsound(sound_file)

play_sound()

# play_sound()


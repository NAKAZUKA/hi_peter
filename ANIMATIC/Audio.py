import pprint
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
import threading

audiofile = 'test.wav'  # path to audiofile

porok_do = 0
porok_posle = 0


def PLAY():
    sound = AudioSegment.from_file(audiofile, format="wav")
    splice = sound
    play(splice)


def PLAY_AUDIO():
    t = threading.Thread(target=PLAY, args=())
    t.start()



def start(starting=0, end=0):
    global porok
    sound = AudioSegment.from_file(audiofile, format="wav")
    splice = sound[(starting * 1000 - porok_do):(end * 1000 + porok_posle)]
    play(splice)


# from Vosk_trunc import start as st
#
# w = st()
# pprint.pprint(w)
# x = w
# for i in x:
#     start(i['start'], i['end'])
#     sleep(i['time'])

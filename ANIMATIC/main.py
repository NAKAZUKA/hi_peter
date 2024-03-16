# import RecFace as rf
import MyFunc as mf
import time

import Anime
import text_to_text as txt
# import Silero as sil
import Vosk_trunc as vt
import text_to_speech as ts

def main(text):
    print('question-answer system')
    result = txt.text_to_text(text)
    # # result = 'Здравствуйте! Санкт-Петербург — один из красивейших городов России. '
    result = mf.pre_tokenizing(result)
    print('--- ' + result)
    #     # print('Silero system')
    #     # sil.start(result, voice='aidar', sample_rate=48000)
    print('text-to-voice system')
    ts.synthesize(result)
    print('Tokenizing system')
    tokens = vt.start()
    print('Anime system')
    # try:
    Anime.start(tokens)
        # while Anime.READY:
        #     time.sleep(1)
    # except Exception as e:
    #     print(e)

    print("OK!!!")
# main('1')
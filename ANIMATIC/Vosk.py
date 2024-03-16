from vosk import Model, KaldiRecognizer
import os
import pyaudio
import main

RATE = 44100
MODEL = 'vosk-model-small-en-us-0.15'  # "vosk-model-small-ru-0.22" - ru, vosk-model-small-en-us-0.15 - eu - vosk-model-en-us-0.42-gigaspeech


def go_anime(audio, stat=''):
    import Anime
    import Vosk_trunc as vt
    import Audio
    Audio.audiofile = 'audio/'+audio+'.wav'
    tokens = vt.start(file='audio/'+audio+'.wav')
    Anime.start(tokens, stat=stat)
    Audio.audiofile = 'test.wav'


QUEST = 0
STATUS = ''


def script(text):
    global QUEST, STATUS
    print("QUEST: " + str(QUEST))
    if QUEST != 0:
        QUEST -= 1

    if QUEST == 0:
        STATUS = ''
    if 'want' in text or STATUS == 'taxi':
        DEF_QUEST = 2
        if QUEST == 0:
            STATUS = 'taxi'
            QUEST = DEF_QUEST
        go_anime('taxi/' + str(DEF_QUEST - QUEST + 1), 'taxi/' + str(DEF_QUEST - QUEST + 1))
        if QUEST == 1:
            go_anime('S', 'taxi/' + str(DEF_QUEST - QUEST + 1))
    elif 'exchange' in text or STATUS == 'exchange':
        DEF_QUEST = 1
        if QUEST == 0:
            STATUS = 'exchange'
            QUEST = DEF_QUEST
        go_anime('money/' + str(DEF_QUEST - QUEST + 1), 'money/' + str(DEF_QUEST - QUEST + 1))
        if QUEST == 1:
            go_anime('S', 'money/' + str(DEF_QUEST - QUEST + 1))
    elif 'sim' in text or STATUS == 'sim':
        DEF_QUEST = 2
        if QUEST == 0:
            STATUS = 'sim'
            QUEST = DEF_QUEST
        go_anime('sim/'+str(DEF_QUEST - QUEST + 1), 'sim/'+str(DEF_QUEST - QUEST + 1))
        if QUEST == 1:
            go_anime('S', 'sim/' + str(DEF_QUEST - QUEST + 1))
    elif text != '':
        go_anime('T', 'T')
        STATUS = ''
        QUEST = 0
        main.main(text)


def start():
    global MODEL, RATE
    model = Model(r"models/vosk/" + MODEL)  # полный путь к модели
    rec = KaldiRecognizer(model, 44100)
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=RATE
    )
    stream.start_stream()

    res = ''
    new_res = ''
    go_anime('HI', 'T')
    while True:
        print('Listening...')
        data = stream.read(RATE)
        if len(data) == 0:
            break
        try:
            res = rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult()
            res = res.replace("\n", '')
            res = res.strip()
            if "\"text\" : \"" in res:
                res = str(res).removesuffix('"}')
                res = str(res).removeprefix('{  "text" : "')

                if res != 'result':
                    print(res)
                    script(res)

        except Exception as e:
            print(e)


    # print(rec.FinalResult())

if __name__ == '__main__':
    start()
import pprint
import wave
import json

from vosk import Model, KaldiRecognizer, SetLogLevel
# import Word as custom_Word

model_path = "models/vosk/vosk-model-small-en-us-0.15"  # vosk-model-small-ru-0.22" - ru, vosk-model-small-en-us-0.15 - en vosk-model-en-us-0.42-gigaspeech
audio_file = "test.wav"
model = Model(model_path)


def start(file='test.wav'):
    print(file)
    # if file == '':
    #     file = audio_file
    wf = wave.open(file, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # get the list of JSON dictionaries
    results = []
    # recognize speech using vosk model
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)
    part_result = json.loads(rec.FinalResult())
    results.append(part_result)

    # convert list of JSON dictionaries to list of 'Word' objects
    list_of_Words = []
    for sentence in results:
        if len(sentence) == 1:
            # sometimes there are bugs in recognition
            # and it returns an empty dictionary
            # {'text': ''}
            continue
        for obj in sentence['result']:
            # w = custom_Word.Word(obj)  # create custom Word object
            list_of_Words.append(obj)  # and add it to list

    wf.close()  # close audiofile

    # output to the screen
    # for word in list_of_Words:
    #     print(word)
    lis = []
    endion = round(list_of_Words[0]['end'])
    for word in list_of_Words:
        l = {}

        ll = {}
        if endion < word['start']:
            ll['time'] = round(word['start'] - endion, 2)
            ll['word'] = '_'
            ll['start'] = endion
            ll['end'] = word['start']
            # ll['conf'] = word['conf']
            lis.append(ll)

        word['end'] = round(word['end'], 2)
        word['start'] = round(word['start'], 2)
        l['time'] = round(word['end'] - word['start'], 2)
        l['word'] = word['word']
        l['start'] = word['start']
        l['end'] = word['end']
        l['conf'] = word['conf']
        lis.append(l)

        endion = word['end']

    return lis


# pprint.pprint(start('test.wav'))

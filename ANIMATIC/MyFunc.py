import os
from pathlib import Path
import pickle

slovar = []
for i in range(ord('A'), ord('Z')):
    slovar.append(chr(i))
    slovar.append(chr(i).lower())
for i in range(ord('А'), ord('Я')):
    slovar.append(chr(i))
    slovar.append(chr(i).lower())
slovar.append('.')
slovar.append(',')


def goToFilesInPath(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    return f


def nameFileWithoutExtension(path):
    return Path(path).stem


def nameFileWithExtension(path):
    return os.path.basename(path).split('/')[-1]


def save_data(file, data):
    with open(file, 'wb') as dump_out:
        pickle.dump(data, dump_out)


def get_data(file):
    with open(file, 'rb') as dump_in:
        der = pickle.load(dump_in)
    return der


def pre_tokenizing(text):
    textion = text
    global slovar
    for i in text:
        if not i in slovar:
            # print("___________________" + i)
            textion.replace(i, '')
    return textion

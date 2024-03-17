# import pprint
from random import randrange, choice
import pygame as pg
import time
import Audio
# from Vosk_trunc import start as st
READY = True
import DATAS as dat
tex = ""

def timing():
    global START_TIME
    # print("--- %s seconds ---" % (time.time() - START_TIME))
    tim = (float(time.time()) - float(START_TIME))
    # print(tim)
    return tim


DATA = []
START_TIME = 0.0
FPS = 60
WIDTHH = 480*2.5
WIDTH = 480
HEIGHT = 640
HEIGHTT = HEIGHT + (HEIGHT // 8)
FRAME = 0
SHAG = 0


def set_image_size(img, height=-1, width=-1):
    import pygame as pg
    if width < 0 and height < 0:
        return img
    if height < 0:
        k = img.get_size()
        return pg.transform.scale(img, (width, round(k[1] / (k[0] / width))))
    elif width < 0:
        k = img.get_size()
        return pg.transform.scale(img, (round(k[0] / (k[1] / height)), height))
    else:
        return pg.transform.scale(img, (width, height))


def CHECK():
    global DATA, START_TIME, SHAG
    # print(DATA)
    for i in range(len(DATA)):
        if DATA[i]['start'] <= timing() <= DATA[i]['end']:
            SHAG = i
            DATA[i]['word'] = (DATA[i]['word']).lower()
            return DATA[i]
    # if DATA == []:
    return 'end'
    # else:
    #     return DATA[i]


def WHAT_CHAR(ch):
    word_time = ch['end'] - ch['start']
    start = ch['start']
    end = ch['end']
    word = ch['word']
    char_time = timing() - ch['start']
    try:
        # print((timing() - start) // (word_time / len(word)))
        return word[int((timing() - start) // (word_time / len(word)))]
    except Exception as e:
        # print(e)
        return '_'






def start(data, stat='', tex=''):
    tex = tex.split()

    global FPS, WIDTH, HEIGHT, FRAME, START_TIME, DATA, READY
    FRAME = 0
    DATA = data
    READY = False

    if not dat.window:
        pg.init()
        window = pg.display.set_mode((WIDTHH, HEIGHT + (HEIGHT // 8)))
        dat.window = window
    else:
        window = dat.window
    if not dat.clock:
        clock = pg.time.Clock()
        dat.clock = clock
    else:
        clock = dat.clock

    logo = pg.image.load('datas/backgrounds/ico.ico')  # directory of logo
    pg.display.set_icon(logo)
    pg.display.set_caption("HI, PETR")


    STATUS = True
    play = True
    CHAR = '_'
    START_TIME = time.time()
    time.sleep(0.2)
    Audio.PLAY_AUDIO()

    Morg = 0
    Morgni = True
    ran = [0.0]
    timess = data[len(data)-1]['end']
    # print(times)
    for _ in range(int(timess) * 5):
        ran.append(float(choice([randrange(0, int(timess*100)), randrange(0, int(timess*100))])) / 100.0)
    # print(ran)

    pg.font.init()
    my_font = pg.font.SysFont('Comic Sans MS', 30)

    # quit()
    while play:
        if CHAR == 'end':
            continue

        try:
            if Morg == 0:
                if ran[0] >= timing():
                    Morgni = 'open'
                else:
                    Morgni = 'close'
                    Morg = 2
                    # print(ran[0], timing())
                    ran.pop(0)
            else:
                Morg -= 1
        except Exception as e:
            Morgni = 'open'
            # print(e)


        # time.sleep(0.1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                play = False

        window.fill((255, 255, 255))

        # if CHAR != 'ending' and CHAR != 'end':
        LAST_CHAR = CHAR
        CHAR = CHECK()

        if str(CHAR).strip() != 'end':
            CHAR = WHAT_CHAR(CHAR)

        if CHAR != '' and LAST_CHAR == CHAR:
            STATUS = True
        else:
            STATUS = False

        if FRAME == 0:
            STATUS = True

        if STATUS:
            body = pg.image.load('datas/Face/Petr/body/1.png')
            body = set_image_size(body, height=HEIGHT)
            body_rect = body.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(body, body_rect)

        # if STATUS or Morgni:
        eye = pg.image.load('datas/Face/Petr/eye/'+Morgni+'.png')
        eye = set_image_size(eye, height=HEIGHT // 13)
        eye_rect = eye.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        height_eye = 7
        width_eye = 13
        right_eye = pg.transform.flip(eye.copy(), True, False)
        window.blit(eye, (eye_rect[0] - (WIDTH // width_eye), eye_rect[0] - (HEIGHT // height_eye)))
        window.blit(right_eye, (eye_rect[0] + (WIDTH // width_eye), eye_rect[0] - (HEIGHT // height_eye)))

        if STATUS:
            eyebrow = pg.image.load('datas/Face/Petr/eyebrow/ok.png')
            eyebrow = set_image_size(eyebrow, height=HEIGHT // 47)
            eyebrow_rect = eyebrow.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            height_eyebrow = 7
            width_eyebrow = 13
            right_eyebrow = pg.transform.flip(eyebrow.copy(), True, False)
        window.blit(eyebrow, (eyebrow_rect[0] - (WIDTH // width_eyebrow), eyebrow_rect[0] - (HEIGHT // height_eyebrow)))
        window.blit(right_eyebrow,
                    (eyebrow_rect[0] + (WIDTH // width_eyebrow), eyebrow_rect[0] - (HEIGHT // height_eyebrow)))

        if STATUS:
            moustache = pg.image.load('datas/Face/Petr/moustache/ok.png')
            moustache = set_image_size(moustache, height=HEIGHT // 37)
            moustache_rect = moustache.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            height_moustache = 38
            width_moustache = 18
            right_moustache = pg.transform.flip(moustache.copy(), True, False)
        window.blit(moustache,
                    (moustache_rect[0] - (WIDTH // width_moustache), moustache_rect[0] - (HEIGHT // height_moustache)))
        window.blit(right_moustache,
                    (moustache_rect[0] + (WIDTH // width_moustache), moustache_rect[0] - (HEIGHT // height_moustache)))

        if STATUS:
            mouth = pg.image.load('datas/Face/Petr/mouth/' + CHAR + '.png')
            mouth = set_image_size(mouth, height=HEIGHT // 19)
            mouth_rect = mouth.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            height_mouth = HEIGHT // -10
            width_mouth = WIDTH
        window.blit(mouth, (mouth_rect[0] - (WIDTH // width_mouth), mouth_rect[0] - (HEIGHT // height_mouth)))

        if stat == '':
            imgi = str(1)
        elif stat == 'T':
            imgi = str(0)
        else:
            imgi = stat
            # print("'"+stat+'"')

        img = pg.image.load('datas/backgrounds/'+imgi+'.jpg')
        img = set_image_size(img, height=HEIGHTT - ((HEIGHTT // 18)*2))
        # print(WIDTHH - int(img.get_width()), 0)
        window.blit(img, (WIDTHH - int(img.get_width()) - (HEIGHTT // 18), HEIGHTT // 18))


        # text_surface = my_font.render(textion, False, (0, 0, 0))
        # # print(text_surface.get_width())
        # window.blit(text_surface, ((WIDTH // 2) - (text_surface.get_width() // 2), HEIGHT))

        # SUBBING
        # print(DATA)
        textion = []
        KOL_WORDS_IN_SUB = 4
        # if tex != []:
        #     KOL_WORDS_IN_SUB = 7
        #     print(tex)
        #     for i in range((SHAG // KOL_WORDS_IN_SUB * KOL_WORDS_IN_SUB), (SHAG // KOL_WORDS_IN_SUB * KOL_WORDS_IN_SUB) + KOL_WORDS_IN_SUB + 1):
        #         textion.append(tex[i])
        # else:
        for i in range((SHAG // KOL_WORDS_IN_SUB * KOL_WORDS_IN_SUB),
                       (SHAG // KOL_WORDS_IN_SUB * KOL_WORDS_IN_SUB) + KOL_WORDS_IN_SUB):
            try:
                CH = DATA[i]['word']
                CH = str(CH).strip().replace('_', '').replace('-', '')
                textion.append(CH)
            except:
                pass
        textion.append('')
        textion = ' '.join(textion)

        text_surface = my_font.render(textion, False, (0, 0, 0))
        # print(text_surface.get_width())
        window.blit(text_surface, ((WIDTH // 2) - (text_surface.get_width() // 2), HEIGHT))

        # SUBBING
        # try:
        #
        #     if str(CHAR['word']).strip() == '_' or str(CHAR['word']).strip() == '-' or str(CHAR['word']).strip() == ' ' or str(CHAR['word']).strip() == '':
        #         textion = textion
        #     else:
        #         textion = str(CHAR['word']).strip()
        # except:
        #     pass



        # if CHAR == 'ending':
        #     eye = pg.image.load('datas/Face/Petr/eye/open.png')
        #     eye = set_image_size(eye, height=HEIGHT // 19)
        #     eye_rect = eye.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        #     height_eye = HEIGHT // -10
        #     width_eye = WIDTH
        #     window.blit(eye, (eye_rect[0] - (WIDTH // width_eye), eye_rect[0] - (HEIGHT // height_eye)))
        #     # pg.quit()
        #     return

        STATUS = False

        FRAME += 1

        # print(clock.get_fps())
        pg.display.update()
        clock.tick(FPS)
        # print(CHAR)
        if CHAR == 'end':
            # pg.quitgame()
            return
    # pg.quit()
# try:
#     start(st())
# except:
#     pass

#UTF-8
# Faralaks Group (c)

# +-----------------------------------------------------------+
# | Старт программы, загрузка составных частей, инициализация | 
# +-----------------------------------------------------------+

# загрузка библиотек
import pygame, webbrowser, random
from pygame import *
from cryptography.fernet import Fernet
from modules import stoper

pygame.init() # инициализация библиотеки pygame

# инициализация переменных
# основные переменные
mode = 'game'
fps_holder = pygame.time.Clock()

# переменные главного меню
menu_button = 1
sound_button = [2, 2]

# переменные игрового процесса
refresh = True
screen_pos = [50, 50]
invisible_objects = {'dungeon'}
ground = pygame.Surface((1320, 760))

# переменные внутриигрового меню


# пероеменная для главного героя. структура: [имя героя, изображение, [координаты на экране], [номер карты], [движение влево, вправо, вверх, вниз], уровень, деньги]
hero = ['name', pygame.image.load('data/pictures/hero.png'), [550,350 ], [0, 0], [False, False, False, False], 1, 999]



# создание функций и классовв
def klick_objects_loader(mode):
    """Загружает кликабельные объекты"""
    done_klick_objects = {}
    file = open('data/klick_objects/' + mode + '.txt')
    for line in file:
        line = line.strip().split(' = ')
        back = []
        for i in line[1].split('+'):
            back.append(i.split('_'))
        done_klick_objects[line[0]] = back
    del back, line, i
    return done_klick_objects

def stoper_loader(map, key=Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=')):
    """Загружает координаты Стопера"""
    adres = 'data/stoper/stoper' + str(map[0]) + '_' + str(map[1]) + '.frls'
    try: file = open(adres)
    except FileNotFoundError:
        return ['']
    else:
        file = open(adres, 'rb')
        return key.decrypt(file.read()).decode('utf8').split('+')

def object_loader(map, key=Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=')):
    """Загружает объекты на карте"""
    adres = 'data/objects/objects' + str(map[0]) + '_' + str(map[1]) + '.frls'
    try: file = open(adres)
    except FileNotFoundError:
        return [['']]
    else:
        file = open(adres, 'rb')
        objects = []
        for object in key.decrypt(file.read()).decode('utf8').split('+'):
            objects.append(object.split('_'))
    return objects

# загрузка изображений
all_pictures = {} # словарь со всеми изображениями кроме Мобов и ГГ 
file = open('data/picture_locations.txt')
for line in file:
    back = []
    line = line.strip().split(' ')
    for i in range(int(line[1])):
        back.append(pygame.image.load(line[2] + str(i + 1) + line[3]))
    all_pictures[line[0]] = back

# загрузка цветовой кодировки
color_codes = {} # словарь с кодировками цветов
file = open('data/color_codes.txt')
for line in file:
    line = line.strip().split(' ')
    color_codes[line[0]] = line[1]

# загрузка карты игрового мира
konva = pygame.image.frombuffer(Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=').decrypt(open('data/map/map.frls', 'rb').read()),(3456 ,3456), 'RGB')
konva_surf = pygame.Surface((3456, 3456))
konva_surf.blit(konva, (0, 0))
konva_pix = pygame.PixelArray(konva_surf)

del back, file, line, i, konva_surf, konva # удаление лишнего

# создание окна игры
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) 
pygame.display.set_caption('Test') # измеенение названия окна


# +--------------+
# | Главное меню |
# +--------------+

while mode == 'main_menu':
    window.blit(all_pictures[mode][menu_button - 1], (0, 0)) # фон
    if menu_button == 2:
        window.blit(all_pictures['sound_button'][sound_button[1] - 1], (920, 323)) # вкл/выкл музыка
        window.blit(all_pictures['sound_button'][sound_button[0] - 1], (920, 357)) # вкл/выкл звук
        
    klick_objects = klick_objects_loader(mode) # загрузки кликабельныз объектов
    # обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            mode = 'Exit'
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                mode = 'Exit'
                menu_button = 3
                
        # события мыши     
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                #print(mouse_pos)
                for klick_object in klick_objects[str(menu_button)]:
                    if int(klick_object[1]) <= mouse_pos[0] <= int(klick_object[3]) and int(klick_object[2]) <= mouse_pos[1] <= int(klick_object[4]):
                        if klick_object[0] == 'options': menu_button = 2
                        elif klick_object[0] == 'exit': menu_button = 3
                        elif klick_object[0] == 'play': menu_button = 1
                        elif klick_object[0] == 'soundbutton':
                            if sound_button[0] == 1: sound_button[0] = 2
                            elif sound_button[0] == 2: sound_button[0] = 1
                        elif klick_object[0] == 'musicbutton':
                            if sound_button[1] == 1: sound_button[1] = 2
                            elif sound_button[1] == 2: sound_button[1] = 1
                        elif klick_object[0] == 'openVK': webbrowser.open('https://vk.com/Faralaks')
                        elif klick_object[0] == 'openYT': webbrowser.open('https://www.youtube.com/Faralaks')
                        elif klick_object[0] == 'openSteam': webbrowser.open('http://steamcommunity.com/id/Faralaks')
                        elif klick_object[0] == 'openWS': webbrowser.open('ms-windows-store://pdp/?productid=9WZDNCRFJ1PT&referrer=unistoreweb&scenario=click&webig=e3428e62-12ab-4149-9556-b329133c2efc&muid=053DBBC097DC6FD0385BB10B93DC6C3E&websession=c2f554163c91413a8bafaf5459efd845')
                        elif klick_object[0] == 'yesexit': mode = 'Exit'
                        elif klick_object[0] == 'save': mode = 'game'
    
    fps_holder.tick(60) # контроль частоты кадров (60 кадров в секунду)
    display.update()



# +-----------------+
# | Игровой процесс |
# +-----------------+

while mode == 'game':
    if refresh == True:
        refresh = False
        stoper = stoper_loader(hero[3]) # загрузка координат стопера
        objects = object_loader(hero[3]) # загрузка объектов на карте
        # генерация  карты
        for pix_y in range(hero[3][1]*36, hero[3][1]*36 + 36):
            for pix_x in range(hero[3][0]*64, hero[3][0]*64 + 64):
                ground.blit(random.choice(all_pictures[color_codes[str(konva_pix[pix_x, pix_y])]]), ((pix_x - hero[3][0]*64)*20, (pix_y - hero[3][1]*36)*20))
        # прорисовка объектов на карте
        if objects != [['']]:
            for object in objects:
                if object[0] in invisible_objects: continue
                ground.blit(all_pictures[object[0]][int(object[1])], (int(object[2]), int(object[3])))

    
    # обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            mode = 'Exit'
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                mode = 'Exit'

            if event.key == K_LEFT or event.key == K_a: hero[4][0] = True
            if event.key == K_RIGHT or event.key == K_d: hero[4][1] = True
            if event.key == K_UP or event.key == K_w: hero[4][2] = True
            if event.key == K_DOWN or event.key == K_s: hero[4][3] = True
        if  event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a: hero[4][0] = False
            if event.key == K_RIGHT or event.key == K_d: hero[4][1] = False
            if event.key == K_UP or event.key == K_w: hero[4][2] = False
            if event.key == K_DOWN or event.key == K_s: hero[4][3] = False
         
    # движение при удержании клавиш 
    if hero[4][0] == True: hero[2][0] -= 3
    if hero[4][1] == True: hero[2][0] += 3
    if hero[4][2] == True: hero[2][1] -= 3
    if hero[4][3] == True: hero[2][1] += 3
    
    # переход в другую область карты
    if hero[2][0] < -25:
        hero[3][0] -= 1
        hero[2][0] = 1255
        refresh = True
    elif hero[2][0] > 1255:
        hero[3][0] += 1
        hero[2][0] = -25
        refresh = True
    elif hero[2][1] < -25:
        hero[3][1] -= 1
        hero[2][1] = 683
        refresh = True
    elif hero[2][1] > 680:
        hero[3][1] += 1
        hero[2][1] = -25
        refresh = True

    
    
    
    window.blit(ground, (0, 0))
    window.blit(hero[1], (hero[2][0], hero[2][1]))
    fps_holder.tick(160) # контроль частоты кадров (60 кадров в секунду)
    display.update()
                




pygame.quit()
print('')
print('DONE!')
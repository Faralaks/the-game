# -*- coding: cp1251 -*-
# Faralaks (c)

# +-----------------------------------------------------------+
# | Старт программы, загрузка составных частей, инициализация | 
# +-----------------------------------------------------------+

# загрузка библиотек
import pygame, webbrowser, random
from pygame import *
from cryptography.fernet import Fernet

pygame.init() # инициализация библиотеки pygame

# инициализация переменных
# основные переменные
mode = 'main_menu'
fps_holder = pygame.time.Clock()

# переменные главного меню
menu_button = 1
sound_button = [2, 2]

# переменные игрового процесса
refresh = True # переменная отвечает за перезагрузку карты
action = False # переменная отвечает за то, применяет ли игрок действие к объекту или нет
invisible_objects = {'dungeon', 'quicksand'} # объекты, которые не прорисовываются на экране
stop_place = {'water', 'dark_water', '4bridge', 'dark_brick', 'dark', '1dark_roof', '2dark_roof', '3dark_roof'} # клетки, которые покрываются Стопером
around_it = {'grass', 'sand', 'dark_grass', 'ashen_earth', 'snow', 'stone', '1bridge', '2bridge', '3bridge', '4bridge', '5bridge', 'dirt'} # клетки, около которых может образоваться Стопер
ground = pygame.Surface((1280, 720))

# переменные внутриигрового меню


# пероеменная для главного героя. структура: [имя героя, изображение, [координаты на экране], [номер карты, открываемые файлы], [движение влево, вправо, вверх, вниз], [размер героя], уровень, деньги]
hero = ['name', pygame.image.load('data/pictures/hero.png'), [200,330 ], [1, 0, 1, 0], [False, False, False, False], [60, 60], 1, 999]



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

def stop_checker(stopers, x, y, size, side):
    """Проверяет, может ли объект двигаться дальше"""
    if stopers != ['']:
        for stoper in stopers:
            stoper = stoper.split('_')
            if stoper == [''] or stoper == '': continue
            if side == 'L' and x + size[0] - 11 >= int(stoper[0]) and x + 8 <= int(stoper[2]) and y + size[1] - 11 >= int(stoper[1]) and y + 39 <= int(stoper[3]): return True
            if side == 'R' and x + size[0] - 8 >= int(stoper[0]) and x + 11 <= int(stoper[2]) and y + size[1] - 11 >= int(stoper[1]) and y + 39 <= int(stoper[3]): return True
            if side == 'U' and x + size[0] - 11 >= int(stoper[0]) and x + 11 <= int(stoper[2]) and y + size[1] - 11 >= int(stoper[1]) and y + 36 <= int(stoper[3]): return True
            if side == 'D' and x + size[0] - 11 >= int(stoper[0]) and x + 11 <= int(stoper[2]) and y + size[1] - 8 >= int(stoper[1]) and y + 39 <= int(stoper[3]): return True
    return False
        
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

# загрузка карты игрового мира и подземелей
konva_surf = pygame.Surface((3456, 3456))
dungeon_surf = pygame.Surface((3456, 3456))
#konva = pygame.image.frombuffer(Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=').decrypt(open('data/map/map.frls', 'rb').read()),(3456 ,3456), 'RGB')
konva = pygame.image.load('data/map/map.png')
konva_surf.blit(konva, (0, 0))
konva_pix = pygame.PixelArray(konva_surf)
#konva = pygame.image.frombuffer(Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=').decrypt(open('data/map/dungeon_map.frls', 'rb').read()),(3456 ,3456), 'RGB')
konva = pygame.image.load('data/map/dungeon_map.png')
dungeon_surf.blit(konva, (0, 0))
dungeon_pix = pygame.PixelArray(dungeon_surf)
map_pix = konva_pix




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
                        elif klick_object[0] == 'save': mode = 'Game'
    
    fps_holder.tick(60) # контроль частоты кадров (60 кадров в секунду)
    display.update()


# +-----------------+
# | Игровой процесс |
# +-----------------+


while mode == 'Game' or mode == 'dungeon':
    if refresh == True:
        refresh = False
        stoper = stoper_loader(hero[3][-2:]) # загрузка координат стопера
        objects = object_loader(hero[3][-2:]) # загрузка объектов на карте
        # генерация  карты
        for pix_y in range(hero[3][1]*36, hero[3][1]*36 + 36):
            for pix_x in range(hero[3][0]*64, hero[3][0]*64 + 64):
                ground.blit(random.choice(all_pictures[color_codes[str(map_pix[pix_x, pix_y])]]), ((pix_x - hero[3][0]*64)*20, (pix_y - hero[3][1]*36)*20))
                # создание Стопера, если клетка из множества stop_place и граничит с клеткой из around_it
                if color_codes[str(map_pix[pix_x, pix_y])] in stop_place and (color_codes[str(map_pix[pix_x - 1, pix_y])] in around_it or color_codes[str(map_pix[pix_x + 1, pix_y])] in around_it or color_codes[str(map_pix[pix_x, pix_y - 1])] in around_it or color_codes[str(map_pix[pix_x, pix_y + 1])] in around_it):
                    stoper.append('_'.join((str((pix_x - hero[3][0]*64)*20), str((pix_y - hero[3][1]*36)*20), str((pix_x - hero[3][0]*64)*20 + 20), str((pix_y - hero[3][1]*36)*20 + 20))))
        
        # прорисовка объектов на карте
        if objects != [['']]:
            for object in objects:
                #if object[0] in invisible_objects: continue
                ground.blit(all_pictures[object[0]][int(object[1]) - 1], (int(object[2]), int(object[3])))
    
    # прорисовка героя
    window.blit(ground, (0, 0))
    window.blit(hero[1], (hero[2][0], hero[2][1]))
    
    # обработка событий
    for event in pygame.event.get(): 
        if event.type == QUIT:
            mode = 'Exit'
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                mode = 'Exit'
            if event.key == K_SPACE:action = True
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
    if hero[4][0] == True and stop_checker(stoper, hero[2][0], hero[2][1], hero[5], 'L') == False: hero[2][0] -= 3
    if hero[4][1] == True and stop_checker(stoper, hero[2][0], hero[2][1], hero[5], 'R') == False: hero[2][0] += 3
    if hero[4][2] == True and stop_checker(stoper, hero[2][0], hero[2][1], hero[5], 'U') == False: hero[2][1] -= 3
    if hero[4][3] == True and stop_checker(stoper, hero[2][0], hero[2][1], hero[5], 'D') == False: hero[2][1] += 3
    
    # переход в другую область карты
    if hero[2][0] < -25:
        hero[3][0] -= 1
        if mode == 'dungeon': hero[3][2] += 1
        else: hero[3][2] -= 1 
        hero[2][0] = 1255
        refresh = True
    elif hero[2][0] > 1255:
        hero[3][0] += 1
        if mode == 'dungeon': hero[3][2] -= 1
        else: hero[3][2] += 1 
        hero[2][0] = -25
        refresh = True
    elif hero[2][1] < -25:
        hero[3][1] -= 1
        if mode == 'dungeon': hero[3][3] += 1
        else: hero[3][3] -= 1 
        hero[2][1] = 677
        refresh = True
    elif hero[2][1] > 680:
        hero[3][1] += 1
        if mode == 'dungeon': hero[3][3] -= 1
        else: hero[3][3] += 1 
        hero[2][1] = -22
        refresh = True

    # результат контакта объекта и ГГ/Монстра
    if objects != [['']]:
        for object in objects:
            if object[0] not in ('dungeon', 'shadow') and  hero[2][0] + 60 >= int(object[2]) and hero[2][0] <= int(object[4]) and hero[2][1] + 60 >= int(object[3]) and hero[2][1] + 50 <= int(object[5]):
                window.blit(all_pictures[object[0]][int(object[1]) - 1], (int(object[2]), int(object[3])))
            
            # проверка на объекты, с которыми можно взаимодействовать
            if len(object) > 7 and object[-1] in ('0', '1') and hero[2][0] + 60 >= int(object[6]) and hero[2][0] <= int(object[8]) and hero[2][1] + 60 >= int(object[7]) and hero[2][1] <= int(object[9]):
                if object[0] == 'dungeon': mode = 'dungeon'; hero[3][2] *= -1; hero[3][3] *= -1; map_pix = dungeon_pix; refresh = True
                if action == True and object[0] == 'dore': mode = 'Game'; hero[3][2] *= -1; hero[3][3] * -1; map_pix = konva_pix; refresh = True
                if action == True and object[0]+object[1] == 'fire2': mode = 'ingame_menu'; menu_button = 7
                if action == True and object[0] == 'tree': mode = 'ingame_menu'; menu_button = 7
    

#   +--------------------+
#   | внутриигровое меню |
#   +--------------------+
    
    if mode == 'ingame_menu': hero[4] = [False, False, False, False]
    while mode == 'ingame_menu':
        window.blit(ground, (0, 0))
        window.blit(all_pictures[mode][menu_button - 1], (0, 0)) # фон
        #klick_objects = klick_objects_loader(mode) # загрузки кликабельныз объектов
        # обработка событий
        for event in pygame.event.get():
            if event.type == QUIT:
                mode = 'Exit'
            if  event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mode = 'Game'
        
        
        
        
        fps_holder.tick(120) # контроль частоты кадров (60 кадров в секунду)
        display.update()
    
    action = False
    fps_holder.tick(120) # контроль частоты кадров (60 кадров в секунду)
    display.update()
                




pygame.quit()
print('')
print('DONE!')
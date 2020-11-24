#UTF-8
# загрузка библиотек
import pygame, webbrowser
from pygame import *
from stoper import stoper # функция отвечающая за колизию объектов

# инициализация
pygame.init() # инициализация библиотеки
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) # создание окна
pygame.display.set_caption('Test') # измеенение названия окна
hero = pygame.image.load('data/pictures/hero.png') # загрузка изображений главного героя
map_name = 'data/maps/lvl1/map' # путь к карте первого уровня
moving = [False, False, False, False,] # разрешения на движения
game_flag = True # флаг главгого игрового цикла
menu_flag = True # флаг главного меню
menu_back = pygame.image.load('data/pictures/2.jpg')
menu_ramka = (pygame.image.load('data/pictures/ramka1.png'), pygame.image.load('data/pictures/ramka2.png'), pygame.image.load('data/pictures/ramka3.png'))
menu_button = 0
a = pygame.image.load('data/pictures/5.png')
a1 = pygame.image.load('data/pictures/8.png')
a2 = pygame.image.load('data/pictures/9.png')
a3 = pygame.image.load('data/pictures/10.png')
a4 = pygame.image.load('data/pictures/11.png')








# пока так
x_hero = 300
y_hero = 100
map_number = [0, 0]
map_level_1 = pygame.image.load('data/maps/lvl1/map0_0l1.jpg')



# главный цикл режима камеры 1
while game_flag:
    # обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            game_flag = False
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_flag = False
            if event.key == K_LEFT or event.key == K_a: moving[0] = True
            if event.key == K_RIGHT or event.key == K_d: moving[1] = True
            if event.key == K_UP or event.key == K_w: moving[2] = True
            if event.key == K_DOWN or event.key == K_s: moving[3] = True
        if  event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a: moving[0] = False
            if event.key == K_RIGHT or event.key == K_d: moving[1] = False
            if event.key == K_UP or event.key == K_w: moving[2] = False
            if event.key == K_DOWN or event.key == K_s: moving[3] = False

    # движение при удержпнии клавиш 
    if moving[0] ==  True and stoper(map_number, x_hero, y_hero, 3): x_hero  -= 3
    if moving[1] ==  True and stoper(map_number, x_hero, y_hero, 2): x_hero  += 3
    if moving[3] ==  True and stoper(map_number, x_hero, y_hero, 0): y_hero  += 3
    if moving[2] ==  True and stoper(map_number, x_hero, y_hero, 1): y_hero  -= 3

     
    # переход в другую область карты
    if x_hero < -25:
        if map_number[0] > 0:
            map_number[0] -= 1
            x_hero = 1305
            map_level_1 = pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + 'l1.jpg')
            #map_level_2 = pygame.image.load(map_name + str(map_number) + 'l2.jpg')
            print(map_number)
        else: x_hero = -25
    elif x_hero > 1305:
        if map_number[0] < 53:
            map_number[0] += 1
            x_hero = -25
            map_level_1 = pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + 'l1.jpg')
            #map_level_2 = pygame.image.load(map_name + str(map_number) + 'l2.jpg')
            print(map_number)
        else: x_hero = 1305
    elif y_hero < -25:
        if map_number[1] > 0:
            map_number[1] -= 1
            y_hero = 755
            map_level_1 = pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + 'l1.jpg')
            #map_level_2 = pygame.image.load(map_name + str(map_number) + 'l2.jpg')
            print(map_number)
        else:  y_hero = -25
    elif y_hero > 755:
        if map_number[1] < 95:
            map_number[1] += 1
            y_hero = -25
            map_level_1 = pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + 'l1.jpg')
            #map_level_2 = pygame.image.load(map_name + str(map_number) + 'l2.jpg')
            print(map_number)
        else: y_hero = 755

        
    # формирование кадра
    window.blit(map_level_1, (0, 0))
    window.blit(hero, (x_hero, y_hero))
    #window.blit(map_level_2, (0, 0))
    display.update()













pygame.quit()

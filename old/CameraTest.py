#UTF-8
#UTF-8
# загрузка библиотек
import pygame
from pygame import *


# инициализация
pygame.init()
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
pygame.display.set_caption('Test')
hero = pygame.image.load('data/pictures/hero.png')
map_level_1 = pygame.image.load('data/pictures/maps/map0_0l1.jpg' )
map_name = 'data/pictures/maps/map'
step = 10
camera_mode = 1


if camera_mode == 1: # первый режим камеры
    moving = [False, False, False, False]
    x_hero = 615
    y_hero = 335
    map_number = [0, 0]
    main1 = True
    #pygame.key.set_repeat(1,1)
    # главный цикл режима камеры 1
    while main1:
        # обработка событий
        for event in pygame.event.get():
            if event.type == QUIT:
                main1 = False
            if  event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main1 = False
                if event.key == K_LEFT:
                    moving[0] = True
                if event.key == K_RIGHT:
                    moving[1] = True
                if event.key == K_UP:
                    moving[2] = True
                if event.key == K_DOWN:
                    moving[3] = True
            if  event.type == KEYUP:
                if event.key == K_LEFT:
                    moving[0] = False
                if event.key == K_RIGHT:
                    moving[1] = False
                if event.key == K_UP:
                    moving[2] = False
                if event.key == K_DOWN:
                    moving[3] = False

        # движение при удержпнии клавиш 
        if moving[0] ==  True: x_hero  -= 2
        if moving[1] ==  True: x_hero  += 2
        if moving[3] ==  True: y_hero  += 2
        if moving[2] ==  True: y_hero  -= 2

        
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
       

elif camera_mode == 2: # второй режим камеры
    x_skreen = 0
    y_skreen = 0
    main2 = True
    pygame.key.set_repeat(1,1)
    # главный цикл  режима камеры 2
    while main2:
        # обработка событий
        for event in pygame.event.get():
            if event.type == QUIT:
                main2 = False
            if  event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main2 = False
                if event.key == K_LEFT:
                    x_skreen += step
                if event.key == K_RIGHT:
                    x_skreen -= step
                if event.key == K_UP:
                    y_skreen += step
                if event.key == K_DOWN:
                    y_skreen -= step

        # формирование кадра
        window.blit(map2_2, (0 + x_skreen, 0 + y_skreen))
        window.blit(map2_2, (-1280 + x_skreen, -720 + y_skreen))
        window.blit(map2_2, (-1280 + x_skreen, 0 + y_skreen))
        window.blit(map2_2, (0 + x_skreen, -720 + y_skreen))
        window.blit(hero, (615, 335))
        display.update()
pygame.quit()

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
menu_back = pygame.image.load('data/pictures/menu_back.jpg') # задник главного меню
picture_menu_ramka = (pygame.image.load('data/pictures/ramka1.png'), pygame.image.load('data/pictures/ramka2.png'), pygame.image.load('data/pictures/ramka3.png')) # рамки главного меню
picture_music_button = (pygame.image.load('data/pictures/picture_sound_button_off.png'), pygame.image.load('data/pictures/picture_sound_button_on.png')) # переключатель  музыки
picture_sound_button = (pygame.image.load('data/pictures/picture_sound_button_off.png'), pygame.image.load('data/pictures/picture_sound_button_on.png')) #переключаьедь звука
pictures_camera_mode_button = (pygame.image.load('data/pictures/pictures_camera_mode1_button.png'), pygame.image.load('data/pictures/pictures_camera_mode2_button.png'), pygame.image.load('data/pictures/pictures_camera_mode3_button.png'), pygame.image.load('data/pictures/pictures_camera_mode4_button.png')) # варианты режимов камеры
menu_button = 0 # нажатая кнопка в главном меню





# пока так
x_hero = 300
y_hero = 100
map_number = [0, 0]
map_level_1 = pygame.image.load('data/maps/lvl1/map0_0l1.jpg')
sound_button = False
music_button = False
camera_mode = 0




# цикл главное меню
while menu_flag:
    window.blit(menu_back, (0, 0)) # фон
    # обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            menu_button = 2
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menu_button = 2
                
        # события мыши     
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # переключение рамок главного меню
                print(pygame.mouse.get_pos())
                if pygame.mouse.get_pos()[0] >= 354 and pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] >= 265 and pygame.mouse.get_pos()[1] <= 350:
                    menu_button = 0
                                        
                elif pygame.mouse.get_pos()[0] >= 356 and pygame.mouse.get_pos()[0] <= 591 and pygame.mouse.get_pos()[1] >= 384 and pygame.mouse.get_pos()[1] <= 461:
                    menu_button = 1
                elif pygame.mouse.get_pos()[0] >= 356 and pygame.mouse.get_pos()[0] <= 596 and pygame.mouse.get_pos()[1] >= 496 and pygame.mouse.get_pos()[1] <= 569:
                    menu_button = 2
                # управление режимом камеры
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 877 and pygame.mouse.get_pos()[0] <= 896 and pygame.mouse.get_pos()[1] >= 318 and pygame.mouse.get_pos()[1] <= 337:
                    camera_mode = 0
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 897 and pygame.mouse.get_pos()[0] <= 916 and pygame.mouse.get_pos()[1] >= 318 and pygame.mouse.get_pos()[1] <= 337:
                    camera_mode = 1
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 917 and pygame.mouse.get_pos()[0] <= 936 and pygame.mouse.get_pos()[1] >= 318 and pygame.mouse.get_pos()[1] <= 337:
                    camera_mode = 2
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 937 and pygame.mouse.get_pos()[0] <= 957 and pygame.mouse.get_pos()[1] >= 318 and pygame.mouse.get_pos()[1] <= 337:
                    camera_mode = 3
                # управление звуком и музыкой
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 930 and pygame.mouse.get_pos()[1] >= 350 and pygame.mouse.get_pos()[1] <= 370:
                    music_button = not music_button
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 930 and pygame.mouse.get_pos()[1] >= 386 and pygame.mouse.get_pos()[1] <= 406:
                    sound_button = not sound_button
                # ссылки в соц сети
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 723 and pygame.mouse.get_pos()[0] <= 763 and pygame.mouse.get_pos()[1] >= 556 and pygame.mouse.get_pos()[1] <= 596:
                    webbrowser.open('https://vk.com/Faralaks')
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 773 and pygame.mouse.get_pos()[0] <= 828 and pygame.mouse.get_pos()[1] >= 556 and pygame.mouse.get_pos()[1] <= 596:
                    webbrowser.open('https://www.youtube.com/Faralaks')
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 840 and pygame.mouse.get_pos()[0] <= 880 and pygame.mouse.get_pos()[1] >= 556 and pygame.mouse.get_pos()[1] <= 596:
                    webbrowser.open('http://steamcommunity.com/id/Faralaks')
                elif menu_button == 1 and pygame.mouse.get_pos()[0] >= 889 and pygame.mouse.get_pos()[0] <= 924 and pygame.mouse.get_pos()[1] >= 556 and pygame.mouse.get_pos()[1] <= 596:
                    webbrowser.open('https://www.microsoft.com/ru-ru/store/p/ЯндексМузыка/9nblggh0cb6d')    
                # подтверждение выхода
                elif menu_button == 2 and pygame.mouse.get_pos()[0] >= 750 and pygame.mouse.get_pos()[0] <= 917 and pygame.mouse.get_pos()[1] >= 417 and pygame.mouse.get_pos()[1] <= 473:
                    menu_flag = False
                    game_flag = False
                
                if menu_button == 0 and pygame.mouse.get_pos()[0] >= 684 and pygame.mouse.get_pos()[0] <= 964 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 587:
                    menu_button = 0
                    menu_flag = False
                    
                    
                
                
    
    
    # прорисовка кадра
    window.blit(picture_menu_ramka[menu_button], (666, 240))
    if menu_button == 1:
        window.blit(pictures_camera_mode_button[camera_mode], (877, 318))
        window.blit(picture_music_button[int(music_button)], (910, 350))
        window.blit(picture_sound_button[int(sound_button)], (910, 386))
    display.update()









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
            x_hero = 1255
            map_level_1 = pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + 'l1.jpg')
        else: x_hero = -25
    elif x_hero > 1255:
        if map_number[0] < 53:
            map_number[0] += 1
            x_hero = -25
            map_level_1 = pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + 'l1.jpg')
        else: x_hero = 1255
    elif y_hero < -25:
        if map_number[1] > 0:
            map_number[1] -= 1
            y_hero = 690
            map_level_1 = pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + 'l1.jpg')
        else:  y_hero = -25
    elif y_hero > 690:
        if map_number[1] < 95:
            map_number[1] += 1
            y_hero = -25
            map_level_1 = pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + 'l1.jpg')
        else: y_hero = 690

        

        
    # формирование кадра
    window.blit(map_level_1, (0, 0))
    window.blit(hero, (x_hero, y_hero))
    #window.blit(map_level_2, (0, 0))
    display.update()













pygame.quit()

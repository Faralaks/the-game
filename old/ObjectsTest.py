#UTF-8
# загрузка библиотек
import pygame, webbrowser, random, os
from pygame import *
from Crypto.Cipher import DES
from modules import stoper, objects_data # функция отвечающая за колизию объектов

# инициализация
pygame.init() # инициализация библиотеки
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) # создание окна
pygame.display.set_caption('Test') # измеенение названия окна
hero = pygame.image.load('data/pictures/hero.png') # загрузка изображений главного героя
map_name = 'data/maps/map' # путь к карте первого уровня
moving = [False, False, False, False,] # разрешения на движения
game_flag = True # флаг главгого игрового цикла
menu_flag = False # флаг главного меню
menu_back = pygame.image.load('data/pictures/menu_back.jpg') # задник главного меню
picture_menu_ramka = (pygame.image.load('data/pictures/ramka1.png'), pygame.image.load('data/pictures/ramka2.png'), pygame.image.load('data/pictures/ramka3.png')) # рамки главного меню
picture_music_button = (pygame.image.load('data/pictures/picture_sound_button_off.png'), pygame.image.load('data/pictures/picture_sound_button_on.png')) # переключатель  музыки
picture_sound_button = (pygame.image.load('data/pictures/picture_sound_button_off.png'), pygame.image.load('data/pictures/picture_sound_button_on.png')) #переключаьедь звука
pictures_camera_mode_button = (pygame.image.load('data/pictures/pictures_camera_mode1_button.png'), pygame.image.load('data/pictures/pictures_camera_mode2_button.png'), pygame.image.load('data/pictures/pictures_camera_mode3_button.png'), pygame.image.load('data/pictures/pictures_camera_mode4_button.png')) # варианты режимов камеры
menu_button = 0 # нажатая кнопка в главном меню
hero_back = pygame.Surface((50, 50))
reload = True
ground = pygame.Surface((1380, 820))
fps_holder = pygame.time.Clock()
game_menu = (pygame.image.load('data/pictures/game_menu_s.png'),
             pygame.image.load('data/pictures/game_menu_u.png'),
             pygame.image.load('data/pictures/game_menu_i.png'),
             pygame.image.load('data/pictures/game_menu_k.png'),
             pygame.image.load('data/pictures/game_menu_z.png'))


pictures = {'1tree1':pygame.image.load('data/pictures/1tree1.png'),
            'tree1':pygame.image.load('data/pictures/tree1.png'),
            '1tree2':pygame.image.load('data/pictures/1tree2.png'),
            'tree2':pygame.image.load('data/pictures/tree2.png')}




save_meta = b'ru74Atbb'
save_meta1 = DES.new(save_meta, DES.MODE_ECB)
del save_meta


# пока так
x_hero = 700
y_hero = 500
map_number = [0, 0]
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
                #print(pygame.mouse.get_pos())
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
                    
                    
                
                
    
    
    # прорисовка кадра главного меню
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
                menu_button = 0
                menu_reload = True
            if event.key == K_SPACE:
                menu_flag = True
                menu_reload = True
                
            if event.key == K_q: menu_flag = True; menu_reload = True; menu_button = 4
            if event.key == K_m: menu_flag = True; menu_reload = True; menu_button = 3
            if event.key == K_e: menu_flag = True; menu_reload = True; menu_button = 2
            if event.key == K_r: menu_flag = True; menu_reload = True; menu_button = 1
            if event.key == K_LEFT or event.key == K_a: moving[0] = True
            if event.key == K_RIGHT or event.key == K_d: moving[1] = True
            if event.key == K_UP or event.key == K_w: moving[2] = True
            if event.key == K_DOWN or event.key == K_s: moving[3] = True
        if  event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a: moving[0] = False
            if event.key == K_RIGHT or event.key == K_d: moving[1] = False
            if event.key == K_UP or event.key == K_w: moving[2] = False
            if event.key == K_DOWN or event.key == K_s: moving[3] = False




    
    
    # если выполнен переход в другую область карты, то задний план меняается
    if reload == True:
        ground.blit(pygame.image.load(map_name + str(map_number[0]) + '_' + str(map_number[1]) + '.jpg'), (50, 50))
        objects = objects_data(map_number, 'objects', save_meta1)
        if len(objects) > 1:
            for object in objects:
                ground.blit(pictures[object[0]], (int(object[1]) + 50, int(object[2]) + 50))
        stop_kords = objects_data(map_number,'stoper', save_meta1)
        window.blit(ground, (-50, -50))
        reload = False
    
    
    
    
    
    
    
    x_old = x_hero; y_old = y_hero # сохранение прежних координат

    # движение при удержпнии клавиш 
    if moving[0] ==  True and stoper(x_hero, y_hero, 3, stop_kords): x_hero  -= 3
    if moving[1] ==  True and stoper(x_hero, y_hero, 2, stop_kords): x_hero  += 3
    if moving[3] ==  True and stoper(x_hero, y_hero, 0, stop_kords): y_hero  += 3
    if moving[2] ==  True and stoper(x_hero, y_hero, 1, stop_kords): y_hero  -= 3

     
    # переход в другую область карты
    if x_hero < -25:
        map_number[0] -= 1
        x_hero = 1255
        reload = True
    elif x_hero > 1255:
        map_number[0] += 1
        x_hero = -25
        reload = True
    elif y_hero < -25:
        map_number[1] -= 1
        y_hero = 690
        reload = True
    elif y_hero > 690:
        map_number[1] += 1
        y_hero = -25
        reload = True







    # цикл внутриигрового меню 
    while menu_flag:
        if menu_reload == True:
            reload = True
            window.blit(ground, (-50, -50))
            window.blit(game_menu[menu_button], (0, 0))
            reload = True
        for event in pygame.event.get():
            if event.type == QUIT:
                game_flag = False
                menu_flag = False
            if  event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu_flag = False
                if event.key == K_SPACE:
                    menu_flag = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #print(pygame.mouse.get_pos())
                    if pygame.mouse.get_pos()[0] >= 174 and pygame.mouse.get_pos()[0] <= 329 and pygame.mouse.get_pos()[1] >= 102 and pygame.mouse.get_pos()[1] <= 131:
                        menu_button = 0
                        
                    elif pygame.mouse.get_pos()[0] >= 336 and pygame.mouse.get_pos()[0] <= 481 and pygame.mouse.get_pos()[1] >= 102 and pygame.mouse.get_pos()[1] <= 131:
                        menu_button = 1
                    elif pygame.mouse.get_pos()[0] >= 489 and pygame.mouse.get_pos()[0] <= 632 and pygame.mouse.get_pos()[1] >= 102 and pygame.mouse.get_pos()[1] <= 131:
                        menu_button = 2
                    elif pygame.mouse.get_pos()[0] >= 643 and pygame.mouse.get_pos()[0] <= 782 and pygame.mouse.get_pos()[1] >= 102 and pygame.mouse.get_pos()[1] <= 131:
                        menu_button = 3
                    elif pygame.mouse.get_pos()[0] >= 793 and pygame.mouse.get_pos()[0] <= 936 and pygame.mouse.get_pos()[1] >= 102 and pygame.mouse.get_pos()[1] <= 131:
                        menu_button = 4
                    elif pygame.mouse.get_pos()[0] >= 947 and pygame.mouse.get_pos()[0] <= 1096 and pygame.mouse.get_pos()[1] >= 102 and pygame.mouse.get_pos()[1] <= 131:
                        game_flag = False
                        menu_flag = False
        fps_holder.tick(60) # контроль частоты кадров (60 кадров в секунду)
        display.update()
        
        
        
    
    
    
    
    
    
    
    
    
    # формирование кадра
    # замена пикселей в след за героем
    # создание массивов с пикселями
    pix = pygame.PixelArray(ground)
    pix_new = pygame.PixelArray(hero_back)
    # замена пикселей
    pix_new[:,:] = pix[x_old + 50:x_old + 100, y_old + 50 : y_old + 100]
    # применение изменений
    del pix, pix_new
    
    # прорисовка
    window.blit(hero_back, (x_old, y_old))
    window.blit(hero, (x_hero, y_hero))
     
     
     
     
    
    
    
    

    if objects != [['']]:
        for i in objects:
            x1 = int(i[1])
            y1 = int(i[2])
            x2 = int(i[3])
            y2 = int(i[4])
            if x_hero + 50 >= x1 and x_hero <= x2 and y_hero + 50 >= y1 and y_hero <= y2:
                window.blit(pictures['1' + i[0]], (int(i[1]), int(i[2])))
        
        
     
    
    
    
    
    display.update()
    #fps_holder.tick(60) # контроль частоты кадров (60 кадров в секунду)
    
    
    
    


    









pygame.quit()

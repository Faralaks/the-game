#UTF-8
# загрузка библиотек
import pygame, webbrowser, random
from pygame import *
from cryptography.fernet import Fernet
from modules import stoper, objects_data # функция отвечающая за колизию объектов

# инициализация
pygame.init() # инициализация библиотеки
hero = pygame.image.load('data/pictures_old/hero.png') # загрузка изображений главного героя
map_name = 'data/maps/map' # путь к карте первого уровня
moving = [False, False, False, False,] # разрешения на движения
game_flag = True # флаг главгого игрового цикла
menu_flag = False # флаг главного меню
menu_back = pygame.image.load('data/pictures_old/menu_back.jpg') # задник главного меню
picture_menu_ramka = (pygame.image.load('data/pictures_old/ramka1.png'), pygame.image.load('data/pictures_old/ramka2.png'), pygame.image.load('data/pictures_old/ramka3.png')) # рамки главного меню
picture_music_button = (pygame.image.load('data/pictures_old/picture_sound_button_off.png'), pygame.image.load('data/pictures_old/picture_sound_button_on.png')) # переключатель  музыки
picture_sound_button = (pygame.image.load('data/pictures_old/picture_sound_button_off.png'), pygame.image.load('data/pictures_old/picture_sound_button_on.png')) #переключаьедь звука
menu_button = 0 # нажатая кнопка в главном меню
hero_back = pygame.Surface((60, 60))
reload = True
do = False
loot_flag = False

ground = pygame.Surface((1400, 840))
fps_holder = pygame.time.Clock()
game_menu = (pygame.image.load('data/pictures_old/game_menu_s.png'),
             pygame.image.load('data/pictures_old/game_menu_u.png'),
             pygame.image.load('data/pictures_old/game_menu_i.png'),
             pygame.image.load('data/pictures_old/game_menu_k.png'),
             pygame.image.load('data/pictures_old/game_menu_z.png'),
             pygame.image.load('data/pictures_old/game_menu_l.png'))

pictures = {'tree1':pygame.image.load('data/pictures_old/tree1.png'),
            'tree2':pygame.image.load('data/pictures_old/tree2.png'),
            'well1':pygame.image.load('data/pictures_old/well1.png'),
            'cactus1':pygame.image.load('data/pictures_old/cactus1.png'),
            'cactus2':pygame.image.load('data/pictures_old/cactus2.png'),
            'stone1':pygame.image.load('data/pictures_old/stone1.png'),
            'tree3':pygame.image.load('data/pictures_old/tree3.png'),
            'fire1':pygame.image.load('data/pictures_old/fire1.png')}


dungeon_mode = False
# вода граничащая с этими клетками будет иметь барер
map_codes = {9109248, 16742400, 7434027, 3681137, 16774656, 64767, 16056574, 16056575, 16122111, 16187647, 16253183, 16318719}
# следующие клетки имеют только один вид
ones = {'water', '1bridge', '2bridge', '3bridge', '4bridge', '5bridge', '6bridge'}


clear = False
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) # создание окна
pygame.display.set_caption('Test') # измеенение названия окна





konva = pygame.image.frombuffer(Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=').decrypt(open('data/map_old/map.frls', 'rb').read()),(3456 ,3456), 'RGB')


options = {}
file = open('data/map_old/options.txt')
for line in file:
    sip = line[:-1].split(' = ')
    for i in ('1', '2', '3', '4'):
        if sip[1] in ones:
            options[sip[0] + i] = pygame.image.frombuffer(Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=').decrypt(open('data/map_old/' + str(sip[1]) + '1' + '.frls', 'rb').read()), (20 , 20), 'RGB')
        else:
            options[sip[0] + i] = pygame.image.frombuffer(Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=').decrypt(open('data/map_old/' + str(sip[1]) + i + '.frls', 'rb').read()), (20 , 20), 'RGB')
file.close()
konva_surf = pygame.Surface((3456, 3456))
konva_surf.blit(konva, (0, 0))
konva_pix = pygame.PixelArray(konva_surf)
del konva_surf, sip, konva, line, file, i




# пока так
x_hero = 200
y_hero = 300
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


pos = [0,0]


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
                do = True
             
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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
        
    
    x_old = x_hero; y_old = y_hero # сохранение прежних координат

    # движение при удержпнии клавиш 
    if moving[0] ==  True and stoper(x_hero, y_hero, 3, stop_cords): x_hero  -= 3
    if moving[1] ==  True and stoper(x_hero, y_hero, 2, stop_cords): x_hero  += 3
    if moving[3] ==  True and stoper(x_hero, y_hero, 0, stop_cords): y_hero  += 3
    if moving[2] ==  True and stoper(x_hero, y_hero, 1, stop_cords): y_hero  -= 3

     
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
        y_hero = 683
        reload = True
    elif y_hero > 680:
        map_number[1] += 1
        y_hero = -25
        reload = True


    # очистка экрана
    if clear == True:
        window.blit(ground, (-60, -60))
        clear = False
    
    # если выполнен переход в другую область карты, то задний план меняается
    if reload == True:
        # генерация нового экрана
        stop_cords = objects_data(map_number,'stoper', Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48='))
        for i in range(64):
            for ii in range(36):
                ground.blit(options[str(konva_pix[i+64*map_number[0], ii+36*map_number[1]]) + random.choice(('1', '2', '3', '4'))],(i*20 + 60,ii*20 + 60))
                if stop_cords != False and konva_pix[i+64*map_number[0], ii+36*map_number[1]] == 14079 and (konva_pix[i+64*map_number[0] - 1, ii+36*map_number[1]] in map_codes or konva_pix[i+64*map_number[0], ii+36*map_number[1] - 1] in map_codes or konva_pix[i+64*map_number[0] + 1, ii+36*map_number[1]] in map_codes or konva_pix[i+64*map_number[0] + 1, ii+36*map_number[1] + 1] in map_codes):
                    stop_cords.append('_'.join((str(i*20), str(ii*20), str(i*20 + 20), str(ii*20 + 20))))
                                    
        objects = objects_data(map_number, 'objects', Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48='))
        if objects != [['']]:
            for object in objects:
                if object[0] == 'dungeon': continue
                ground.blit(pictures[object[0]], (int(object[1]) + 60, int(object[2]) + 60))
        
        window.blit(ground, (-60, -60))
        reload = False
    



    # цикл внутриигрового меню 
    while menu_flag:
        if menu_reload == True:
            reload = True
            window.blit(ground, (-60, -60))
            window.blit(game_menu[menu_button], (0, 0))
            reload = True
            moving = [False, False, False, False]
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
    pix_new[:,:] = pix[x_old + 60:x_old + 120, y_old + 60 : y_old + 120]
    # применение изменений
    del pix, pix_new
    # прорисовка
    window.blit(hero_back, (x_old, y_old))
    window.blit(hero, (x_hero, y_hero))
     
     
            
    
    
    
    if objects != [['']]:
        for i in objects:
            if i[0] == 'dungeon' and x_hero + 60 >= int(i[1]) and x_hero <= int(i[3]) and y_hero + 60 >= int(i[2]) and y_hero <= int(i[4]):
                dungeon_mode = True

            
            if i[0] == 'dungeon' or i[0] == 'sand': continue
            if x_hero + 60 >= int(i[1]) and x_hero <= int(i[3]) and y_hero + 60 >= int(i[2]) and y_hero + 50 <= int(i[4]):
                window.blit(pictures[i[0]], (int(i[1]), int(i[2])))
                
               
            
            if do == True and i[-1] == '1':
                if i[0] == 'tree1' and x_hero - 10 >= int(i[1]) and x_hero + 60 <= int(i[3]) and y_hero - 110 >= int(i[2]) and y_hero + 10 <= int(i[4]):
                    loot_flag = True
                    window.blit(ground, (-60, -60))
                    window.blit(game_menu[-1], (0, 0))
                    while loot_flag:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                game_flag = False
                                loot_flag = False
                            if  event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    loot_flag = False
                                    clear = True
                                    moving = [False, False, False, False,]
                                    
                                    
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    print(pygame.mouse.get_pos())
                                    if pygame.mouse.get_pos()[0] >= 174 and pygame.mouse.get_pos()[0] <= 329 and pygame.mouse.get_pos()[1] >= 102 and pygame.mouse.get_pos()[1] <= 131:
                                        menu_button = 0
                        fps_holder.tick(60) # контроль частоты кадров (60 кадров в секунду)
                        display.update()
        do = False
        
        
     
    
    
    
    fps_holder.tick(60) # контроль частоты кадров (60 кадров в секунду)
    display.update()

    
    
    
    


    









pygame.quit()

#UTF-8
import pygame, random, os
from pygame import *
from cryptography.fernet import Fernet

pygame.init()
key = Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=')
pict = {}
view = []
view_map = []
data = {}
fps_holder = pygame.time.Clock()
main = True
mode = 'obj'

def stoper_loader(map, key=key):
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
        return []
    else:
        file = open(adres, 'rb')
        objects = []
        for object in key.decrypt(file.read()).decode('utf8').split('+'):
            objects.append(object.split('_'))
    return objects

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
    view_map.append(line[0])
    

file = open('data/objects_data.txt') # данные об объекте
for line in file:
    temp = line.strip().split(', ')
    data[temp[0]] = temp
    view.append(temp[0])
    pict[temp[0]] = pygame.image.load('data/pictures/' + temp[0] + '.png')


# загрузка карты игрового мира
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

del temp, back, file, line, i, konva_surf, konva, dungeon_surf # удаление лишнего


#pygame.mouse.set_visible(False) # нивидимый курсор

remap = True
ground = pygame.Surface((1320, 760))
map = [0, 0, 0 , 0]
# создание окна игры
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) 
pygame.display.set_caption('UME2') # измеенение названия окна
invisible_objects = {'dungeon', 'quicksand'}
fn = False
clear = False
put_to_obj = []
put_to_st = []
with_shadows = {'cactus', 'stone', 'tree', 'well'}
dun = False
klick = False
while main:
    if clear == True:
        clear = False
        # генерация  карты
        for pix_y in range(abs(map[1])*36, abs(map[1])*36 + 36):
            for pix_x in range(abs(map[0])*64, abs(map[0])*64 + 64):
                ground.blit(random.choice(all_pictures[color_codes[str(map_pix[pix_x, pix_y])]]), ((pix_x - abs(map[0])*64)*20, (pix_y - abs(map[1])*36)*20))
    
    if remap == True:
        remap = False
        objects = object_loader(map[-2:]) # загрузка объектов на карте
        # генерация  карты
        for pix_y in range(map[1]*36, map[1]*36 + 36):
            for pix_x in range(map[0]*64, map[0]*64 + 64):
                ground.blit(random.choice(all_pictures[color_codes[str(map_pix[pix_x, pix_y])]]), ((pix_x - map[0]*64)*20, (pix_y - map[1]*36)*20))
        reobj = True
    
    if reobj == True:
        reobj = False
        # прорисовка объектов на карте
        if objects != [['']]:
            for object in objects:
                ground.blit(all_pictures[object[0]][int(object[1]) - 1], (int(object[2]), int(object[3])))
        
                
    # обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            main = False
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                main = False
                
            if event.key == K_c:
                mode = 'map'
                place_pos = [0, 0]
                clear = True
                save_surf = pygame.Surface((3456, 3456))
                
            if event.key == K_e:
                map[2] *= -1
                map[3] *= -1
                dun = not dun
                if map_pix == dungeon_pix: map_pix = konva_pix
                elif map_pix == konva_pix: map_pix = dungeon_pix
                remap = True; reobj = True
                
            if (event.key == K_LEFT or event.key == K_a) and map[0] > 0:
                map[0] -= 1
                if dun: map[2] += 1
                else: map[2] -= 1
                remap = True
            if (event.key == K_RIGHT or event.key == K_d) and map[0] < 53:
                map[0] += 1
                if dun: map[2] -= 1
                else: map[2] += 1
                remap = True
            if (event.key == K_UP or event.key == K_w) and map[1] > 0:
                map[1] -= 1
                if dun: map[3] += 1
                else: map[3] -= 1
                remap = True
            if (event.key == K_DOWN or event.key == K_s) and map[1] < 95:
                map[1] += 1
                if dun: map[3] -= 1
                else: map[3] += 1
                remap = True
                
            if event.key == K_f: fn = not fn
            if event.key == K_BACKSPACE and len(objects) > 0:
                objects.pop(-1)
                reobj = True
                clear = True
            if event.key == K_SPACE:
                objects.clear()
                reobj = True
                clear = True
                
            if event.key == K_q and objects != []:
                file_obj = open('data/objects/objects' + str(map[2]) + '_' + str(map[3]) + '.frls', 'wb')
                file_st = open('data/stoper/stoper' + str(map[2]) + '_' + str(map[3]) + '.frls', 'wb')
                for object in objects:
                    put_to_obj.append('_'.join(object))
                    temp = data[object[0] + object[1]]
                    if object[0] in invisible_objects or object[0] == 'shadow': continue
                    put_to_st.append('_'.join([str(int(object[2]) + int(temp[1])), str(int(object[3]) + int(temp[2])), str(int(object[2]) + int(temp[3])), str(int(object[3]) + int(temp[4]))]))
                file_obj.write(key.encrypt('+'.join(put_to_obj).encode('utf8')))
                file_st.write(key.encrypt('+'.join(put_to_st).encode('utf8')))
                file_obj.close()
                file_st.close()
                
                put_to_obj = []
                put_to_st = []
                
            if event.key == K_q and objects == [] and os.path.exists(os.getcwd() + r'\data\stoper\stoper' + str(map[2]) + '_' + str(map[3]) + '.frls') and os.path.exists(os.getcwd() + r'\data\objects\objects' + str(map[2]) + '_' + str(map[3]) + '.frls'):
                os.remove(os.getcwd() + r'\data\objects\objects' + str(map[2]) + '_' + str(map[3]) + '.frls')
                os.remove(os.getcwd() + r'\data\stoper\stoper' + str(map[2]) + '_' + str(map[3]) + '.frls')
                
                
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                reobj = True
                temp = data[view[0]]
                if temp[0] in invisible_objects: fn = True
                if len(temp) > 9:
                    objects.append([temp[0][:-1], str(temp[0][-1]), str(pos[0]), str(pos[1]), str(int(temp[5]) + pos[0]), str(int(temp[4]) + pos[1]), str(int(temp[6]) + pos[0]), str(int(temp[7]) + pos[1]), str(int(temp[8]) + pos[0]), str(int(temp[9]) + pos[1]), str(int(fn))])
                
                else:
                    objects.append([temp[0][:-1], str(temp[0][-1]), str(pos[0]), str(pos[1]), str(int(temp[5]) + pos[0]), str(int(temp[4]) + pos[1]), str(int(fn))])
                fn = False
                if view[0][:-1] in with_shadows:
                    temp2 = temp[-3:-1]
                    temp = data[temp[-1]]
                    objects.insert(0, [temp[0][:-1], str(temp[0][-1]), str(pos[0] + int(temp2[0])), str(pos[1] + int(temp2[1])), str(int(temp[5]) + pos[0]), str(int(temp[4]) + pos[1]), str(int(fn))])
        
        
        
            if event.button == 4:
                temp = view.pop(-1)
                view.insert(0, temp)
                while view[0][:-1] == 'shadow':
                    temp = view.pop(-1)
                    view.insert(0, temp)
            if event.button == 5:
                temp = view.pop(0)
                view.append(temp)
                while view[0][:-1] == 'shadow':
                    temp = view.pop(0)
                    view.append(temp)


    while mode == 'map':
        if clear == True:
            clear = False
            # генерация  карты
            for pix_y in range(abs(map[1])*36, abs(map[1])*36 + 36):
                for pix_x in range(abs(map[0])*64, abs(map[0])*64 + 64):
                    ground.blit(random.choice(all_pictures[color_codes[str(map_pix[pix_x, pix_y])]]), ((pix_x - abs(map[0])*64)*20, (pix_y - abs(map[1])*36)*20))
    
        if klick:
            map_pix[map[0]*64 + place_pos[0], map[1]*36 + place_pos[1]] = int(view_map[0])
            ground.blit(all_pictures[color_codes[view_map[0]]][0], (place_pos[0]*20, place_pos[1]*20))
        for event in pygame.event.get():
            if event.type == QUIT:
                main = False
                mode = 'obj'
            if  event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mode = 'obj'
                    remap = True
                if event.key == K_SPACE:
                    map_pix[map[0]*64 + place_pos[0], map[1]*36 + place_pos[1]] = int(view_map[0])
                    clear = True
                if event.key == K_q:
                    save_pix = pygame.PixelArray(save_surf)
                    save_pix[:,:] = map_pix[:,:]
                    del save_pix
                    if dun:
                        pygame.image.save(save_surf, 'data/map/dungeon_map.png')
                    else:
                        pygame.image.save(save_surf, 'data/map/map.png')
                    del save_surf
                
                
                if event.key == K_a and map[0] > 0:
                    map[0] -= 1
                    if dun: map[2] += 1
                    else: map[2] -= 1
                    clear = True
                if event.key == K_d and map[0] < 53:
                    map[0] += 1
                    if dun: map[2] -= 1
                    else: map[2] += 1
                    clear = True
                if event.key == K_w and map[1] > 0:
                    map[1] -= 1
                    if dun: map[3] += 1
                    else: map[3] -= 1
                    clear = True
                if event.key == K_s and map[1] < 95:
                    map[1] += 1
                    if dun: map[3] -= 1
                    else: map[3] += 1
                    clear = True
        
                if event.key == K_LEFT: place_pos[0] -= 1
                if event.key == K_RIGHT: place_pos[0] += 1
                if event.key == K_UP: place_pos[1] -= 1
                if event.key == K_DOWN: place_pos[1] += 1
        
                if event.key == K_c:
                    mode = 'obj'
                    remap = True
                if event.key == K_e:
                    map[2] *= -1
                    map[3] *= -1
                    dun = not dun
                    if map_pix == dungeon_pix: map_pix = konva_pix
                    elif map_pix == konva_pix: map_pix = dungeon_pix
        
        
            if event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                place_pos[0] = pos[0] // 20
                place_pos[1] = pos[1] // 20
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    klick = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    klick = True
            
                    
                
                
                if event.button == 4:
                    temp = view_map.pop(-1)
                    view_map.insert(0, temp)
                if event.button == 5:
                    temp = view_map.pop(0)
                    view_map.append(temp)
        window.blit(ground, (0, 0))
        window.blit(all_pictures[color_codes[view_map[0]]][0], (place_pos[0]*20, place_pos[1]*20))
        fps_holder.tick(120) # контроль частоты кадров (60 кадров в секунду)
        display.update()
    window.blit(ground, (0, 0))
    window.blit(pict[view[0]], (pos))
    if fn == True: window.blit(pict['dungeon1'], (1240, 0))
    fps_holder.tick(60) # контроль частоты кадров (60 кадров в секунду)
    display.update()


pygame.quit()
print('')
print('DONE!')
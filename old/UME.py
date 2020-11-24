#UTF-8
import pygame
from pygame import *
from cryptography.fernet import Fernet

pygame.init()
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
main = True
map = [0,0]
wheel = 0
date = {}
num = []
pict = {}
surf1 = pygame.Surface((1280, 720))
surf2 = pygame.Surface((1280, 720))



file_date = open('objects.txt')
for line in file_date:
    dtemp1 = line[:-1].split(', ')
    date[dtemp1[0]] = dtemp1
    num.append(dtemp1[0])
    pict[dtemp1[0]] = pygame.image.load('pictures/' + dtemp1[0] + '.png')
del dtemp1


file_date.close()



key = Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=')


fps_holder = pygame.time.Clock()


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text
def depad(text):
    depad = []
    for depadtemp in text:
        depad.append(depadtemp.strip())
    return depad

pygame.mouse.set_visible(False)
remap = True
nofile = False
refile = True
objects = []
reobj = False
objectstemp = []
fn = False
put = []
stopers = []
sput = []



konva = pygame.image.fromstring(key.decrypt(open('map/map.frls', 'rb').read()), (3456 , 3456), 'RGB')
options = {}
file = open('map/options.txt')
for line in file:
    sip = line[:-1].split(' = ')
    options[sip[0]] = pygame.image.load('mat/sostav_karti/' + str(sip[1]) + '1.png')
file.close()
konva_surf = pygame.Surface((3456, 3456))
konva_surf.blit(konva, (0, 0))
konva_pix = pygame.PixelArray(konva_surf)





while main:
    if remap == True:
        for i in range(64):
            for ii in range(36):
                surf2.blit(options[str(konva_pix[i+64*map[0], ii+36*map[1]])],(i*20,ii*20))
        
        
        
        
        #surf1.blit(map_pict, (0,0))
        #surf2.blit(map_pict, (0,0))
        remap = False
    if reobj == True: objects = []; reobj = False
        
            
    
    
    if refile == True:
        adres = 'objects/objects' + str(map[0]) + '_' + str(map[1]) + '.frls'
        try: file_obj = open(adres)
        except FileNotFoundError:
            nofile = True
        else:
            nofile = False
            file_obj = open(adres, 'rb')
            if len(file_obj.read()) == 0:
                nofile = True  
                file_obj.close()
        if nofile == False:
            file_obj = open(adres, 'rb')
            objects = []
            depaded = key.decrypt(file_obj.read()).decode('utf8').strip().split('+')
            file_obj.close()
            for i in range(len(depaded)):
                objects.append(depaded[i].split('_'))
        else: objects = []

            
        klick = True
        refile = False

    if klick == True:
        klick = False
        if len(objects) > 0:
            for object in objects:
                surf2.blit(pygame.image.load('pictures/' +  object[0] +  object[1] + '.png'), (int(object[1]), int(object[2])))
     
    

    
    
    window.blit(surf2, (0,0))
    for event in pygame.event.get():
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                main = False
            
            
            if event.key == K_BACKSPACE:
                if len(objects) > 0:
                    objects.pop(-1)
                    remap = True
                    klick = True
            if event.key == K_SPACE:
                objects.clear()
                remap = True
                klick = True
            
            
            
            
            if event.key == K_q:
                file = open('objects/objects' + str(map[0]) + '_' + str(map[1]) + '.frls', 'wb')
                filest = open('stoper/stoper' + str(map[0]) + '_' + str(map[1]) + '.frls', 'wb')
                for i in objects:
                    put.append('_'.join(i))
                    dtemp = date[i[0]+i[1]]
                    if i[0] == 'dungeon' or i[0] == 'sand': continue
                    ptemp = [str(int(i[1]) + int(dtemp[1])), str(int(i[2]) + int(dtemp[2])), str(int(i[1]) + int(dtemp[3])), str(int(i[2]) + int(dtemp[4]))]
                    sput.append('_'.join(ptemp))
                file.write(key.encrypt(pad('+'.join(put)).encode('utf8')))
                filest.write(key.encrypt(pad('+'.join(sput)).encode('utf8')))
                file.close()
                filest.close()
                
                put = []
                sput = []
            
            
            if event.key == K_f: fn = not fn
            
            if (event.key == K_LEFT or event.key == K_a) and map[0] != 0: map[0] -= 1; refile = True; remap = True; reobj = True
            if (event.key == K_RIGHT or event.key == K_d) and map[0] < 53: map[0] += 1;  refile = True; remap = True; reobj = True
            if (event.key == K_UP or event.key == K_w) and map[1] > 0: map[1] -= 1;  refile = True; remap = True; reobj = True
            if (event.key == K_DOWN or event.key == K_s) and map[1] < 95: map[1] += 1; refile = True; remap = True; reobj = True
            
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                remap = True
                klick = True
                dtemp = date[num[0]]
                if dtemp[0] == 'dungeon': fn = True
                inobj = [dtemp[0][:-1], str(dtemp[0][-1]), str(pos[0]), str(pos[1]), str(int(dtemp[5]) + pos[0]), str(int(dtemp[4]) + pos[1]), str(int(fn))]
                print(inobj)
                objects.append(inobj)
                
                del inobj, dtemp
                fn = False
                
                
            if event.button == 4: 
                ntemp = num.pop(-1)
                num.insert(0, ntemp)
                del ntemp
            if event.button == 5:
                ntemp = num.pop(0)
                num.append(ntemp)
                del ntemp

    fps_holder.tick(60)
    window.blit(pict[num[0]], (pos[0], pos[1]))
    
    display.flip()
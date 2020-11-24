#UTF-8
import pygame
from pygame import *
fps_holder = pygame.time.Clock()
pygame.init() # инициализация библиотеки
adsq = (int(input('ширина ')) + 40, int(input("высота ")) + 40)
adsqq = input("картина ")
adsqqs = input("тень ")
window = pygame.display.set_mode(adsq)
main = True
map = [0,0]
wheel = 0
map_pict = pygame.image.load(adsqq + '.png')
if adsqqs != '': s_pict = pygame.image.load(adsqqs + '.png')
f = False
visible = False
pos = [0,0]
while main:
    window.fill((100,141,73))

    for event in pygame.event.get():
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                main = False
            if event.key == K_SPACE:
                f = not f
                visible = not visible
                pygame.mouse.set_visible(not visible)
            if f== True and event.key == K_LEFT or event.key == K_a: pos[0]  -= 1
            if f== True and  event.key == K_RIGHT or event.key == K_d: pos[0]  += 1
            if f== True and  event.key == K_UP or event.key == K_w: pos[1]  -= 1
            if f== True and  event.key == K_DOWN or event.key == K_s: pos[1]  += 1
            if event.key == K_f: print(pos)

                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                print(pygame.mouse.get_pos())
        if event.type == MOUSEMOTION:
            pos = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
    if f == True: window.blit(s_pict, (pos))
    window.blit(map_pict, (0,0))
    fps_holder.tick(30)
    display.flip()
    
pygame.quit()
input()

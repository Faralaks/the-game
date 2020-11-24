import pygame, pyperclip
from pygame import *
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) # создание окна
pygame.display.set_caption('MCO') # измеенение названия окна
window.blit(pygame.image.load(pyperclip.paste()), (0, 0))
fps_holder = pygame.time.Clock()
a = True
aa = 1
while a:
    for event in pygame.event.get():
        if event.type == QUIT:
            a = False
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                a = False
                
        # события мыши     
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                if aa == 2:
                    pos2 = pygame.mouse.get_pos()
                    print(str(pos[0]) + '_' + str(pos[1]) + '_' + str(pos2[0]) + '_' + str(pos2[1]))
                else:
                    pos = pygame.mouse.get_pos()
                    print(str(pos[0]) + '_' + str(pos[1]))
                aa += 1
                if aa == 3:
                    aa = 1
                    print('')

    fps_holder.tick(30)
    display.update()
pygame.quit()
input()

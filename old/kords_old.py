#UTF-8
import pygame
from pygame import *
fps_holder = pygame.time.Clock()
pygame.init() # инициализация библиотеки
window = pygame.display.set_mode((int(input()), int(input())))
main = True
map = [0,0]
wheel = 0
map_pict = pygame.image.load(input() + '.png')
window.fill((255,255,255))
window.blit(map_pict, (0,0))
display.flip()
while main:
    for event in pygame.event.get():
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                main = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(pygame.mouse.get_pos())
    fps_holder.tick(10)
    
pygame.quit()

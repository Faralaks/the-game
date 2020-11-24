import pygame
from pygame import *
pygame.init()
while True:
    

    a = input('введите цвет в RGB ')
    w = pygame.display.set_mode((1, 1))
    w.fill((255,0,0))
    c = a.split(' ')
    c = (int(c[0]), int(c[1]), int(c[2]))
    p= pygame.PixelArray(w)
    p[:,:] = c
    print(p[0,0])
    del p
    pygame.quit()


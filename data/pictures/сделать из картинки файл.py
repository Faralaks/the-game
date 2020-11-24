#UTF-8
import pygame, datetime
from pygame import *
from cryptography.fernet import Fernet
now = datetime.datetime.now()



def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text



save_meta1 = Fernet(b'xGsCGQLymuFmwqqsdD3Pj7cAqXhkbVOJcei01O7vO48=')

asd = input()
if asd[-1] == '1':
    for i in ('1', '2', '3', '4'):
        
        konva = pygame.image.load(asd[:-1] + i + '.png')





        a = pygame.image.tostring(konva, 'RGB')

        encrypted_text = save_meta1.encrypt(a)


        f = open(asd[:-1] + i + '.frls','wb')
        f.write(encrypted_text)
        #input()
        f.close()
else:
    konva = pygame.image.load(asd +  '.png')


    a = pygame.image.tostring(konva, 'RGB')

    encrypted_text = save_meta1.encrypt(a)


    f = open(asd + '.frls','wb')
    f.write(encrypted_text)
    input()
    f.close()








# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:53:26 2021

@author: Aziz
"""


import pygame
import sys


pygame.init()
showScreen = pygame.display.set_mode((500,250))
pygame.display.update()
pygame.display.set_caption('Aziz Snake game')
gamePlay = True

while gamePlay:
    for e in pygame.event.get():
        print(e) #print actions 
        

pygame.quit()
sys.exit()
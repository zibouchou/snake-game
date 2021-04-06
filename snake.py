# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:53:26 2021

@author: Aziz
"""


import pygame
import sys


pygame.init()
showScreen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Aziz Snake game')

backColor = (255,255,255)
snakeColor = (0,0,255)
foodColor = (255,0,0)

gamePlay = False

while not gamePlay:
    for e in pygame.event.get():
        print(e) #print actions
        if e.type == pygame.QUIT:
            gamePlay = True
    showScreen.fill(backColor)
    pygame.draw.rect(showScreen, snakeColor, [200,150,10,10])
    pygame.display.update()
        

pygame.quit()
sys.exit()
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

#coordinates

x = 300
y = 300

#when coordinates will change
newX = 0       
newY = 0

clock = pygame.time.Clock()

while not gamePlay:
    for e in pygame.event.get():
        print(e) #print actions
        if e.type == pygame.QUIT:
            gamePlay = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                newX = -10
                newY = 0
            elif e.key == pygame.K_RIGHT:
                newX = 10
                newY = 0
            elif e.key == pygame.K_UP:
                newX = 0
                newY = -10
            elif e.key == pygame.K_DOWN:
                newX = 0
                newY = 10
    
    x += newX
    y += newY
    showScreen.fill(backColor)
    pygame.draw.rect(showScreen, snakeColor, [x,y,10,10])
    pygame.display.update()
    
    clock.tick(30)
        

pygame.quit()
sys.exit()
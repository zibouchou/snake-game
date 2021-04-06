# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:53:26 2021

@author: Aziz
"""


import pygame
import sys
import time
import snakeFunctions as sf


pygame.init()
screenWidth = 800
screenHeight = 600
showScreen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption('Aziz Snake game')

backColor = (255,255,255)
snakeColor = (0,0,255)
loseColor = (255,0,0)
foodColor = (0,255,0)

snakeMoveSize = 10

gamePlay = False

#coordinates

x = screenWidth / 2
y = screenHeight / 2

#when coordinates will change
newX = 0       
newY = 0

clock = pygame.time.Clock()
snakeSpeed = 30

while not gamePlay:
    for e in pygame.event.get():
        print(e) #print actions
        if e.type == pygame.QUIT:
            gamePlay = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                newX = -snakeMoveSize
                newY = 0
            elif e.key == pygame.K_RIGHT:
                newX = snakeMoveSize
                newY = 0
            elif e.key == pygame.K_UP:
                newX = 0
                newY = -snakeMoveSize
            elif e.key == pygame.K_DOWN:
                newX = 0
                newY = snakeMoveSize
                
    if x >= screenWidth or x < 0 or y >= screenHeight or y < 0:
        gamePlay = True
    
    x += newX
    y += newY
    showScreen.fill(backColor)
    pygame.draw.rect(showScreen, snakeColor, [x, y, snakeMoveSize, snakeMoveSize])
    pygame.display.update()
    
    clock.tick(snakeSpeed)
    
sf.showMessage("You lost", showScreen, screenWidth, screenHeight, loseColor)
pygame.display.update()
time.sleep(2)
        

pygame.quit()
sys.exit()
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:53:26 2021

@author: Aziz
"""


import pygame
import sys
import time
import random
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
scoreColor = (255, 255, 102)

snakeMoveSize = 10

clock = pygame.time.Clock()
snakeSpeed = 10

fontStyle = pygame.font.SysFont("bahnschrift", 25)
scoreFont = pygame.font.SysFont("comicsansms", 35)


def game():
    
    gameOver = False
    gameClose = False
    
    #coordinates
    x = screenWidth / 2
    y = screenHeight / 2

    #when coordinates will change
    newX = 0       
    newY = 0
    
    snakeList = []
    lengthSnake = 1
    
    foodx = round(random.randrange(0, screenWidth - snakeMoveSize) / 10.0) * 10.0
    foody = round(random.randrange(0, screenHeight - snakeMoveSize) / 10.0) * 10.0

    while not gameOver:
        
        while gameClose == True:
            showScreen.fill(backColor)
            sf.showMessage("You Lost! Press Q-Quit or C-Play Again", showScreen, screenWidth, screenHeight, loseColor)
            sf.your_score(showScreen, lengthSnake - 1, scoreFont, scoreColor)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        game()
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gameOver = True
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
            gameClose = True
    
        x += newX
        y += newY
        showScreen.fill(backColor)
        pygame.draw.rect(showScreen, foodColor, [foodx, foody, snakeMoveSize, snakeMoveSize])
        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        if len(snakeList) > lengthSnake:
            del snakeList[0]
 
        for xSnake in snakeList[:-1]:
            if xSnake == snakeHead:
                gameClose = True
 
        sf.drawSnake(showScreen, snakeMoveSize, snakeList, snakeColor)
        sf.your_score(showScreen, lengthSnake - 1, scoreFont, scoreColor)
 
        pygame.display.update()
 
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, screenWidth - snakeMoveSize) / 10.0) * 10.0
            foody = round(random.randrange(0, screenHeight - snakeMoveSize) / 10.0) * 10.0
            lengthSnake += 1
    
        clock.tick(snakeSpeed)
    
        
    pygame.display.update()
    time.sleep(2)
        

    pygame.quit()
    sys.exit()
    
game()
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:12:08 2021

@author: Aziz
"""
import pygame

def showMessage(message, showScreen, screenWidth, screenHeight, color):
    font_style = pygame.font.SysFont(None, 30)
    mesg = font_style.render(message, True, color)
    showScreen.blit(mesg, [screenWidth/2, screenHeight/2])
    
def drawSnake(showScreen, snakeMoveSize, snakeList, snakeColor):
    for x in snakeList:
        pygame.draw.rect(showScreen, snakeColor, [x[0], x[1], snakeMoveSize, snakeMoveSize])
        
def your_score(showScreen, score, scoreFont, scoreColor):
    value = scoreFont.render("Your Score: " + str(score), True, scoreColor)
    showScreen.blit(value, [0, 0])
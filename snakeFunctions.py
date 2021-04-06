# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:12:08 2021

@author: Aziz
"""
import pygame

def showMessage(message, showScreen, screenWidth, screenHeight, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(message, True, color)
    showScreen.blit(mesg, [screenWidth/2, screenHeight/2])
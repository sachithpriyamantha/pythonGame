import pygame
import sys
import os 
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

#we will declare globale constant definition

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE # we will keep both food and size of snake same
SEPARATION = 10 #separation between two pixels
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP":1 , "DOWN":2 , "LEFT":3, "RIGHT":4}

#WE WILL INITIALISE SCREEN
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT),pygame.HWSURFACE)

score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
score_over_font = pygame.font.Font(None,40)
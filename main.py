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
game_over_font = pygame.font.Font(None,40)
play_again_font = score_numb_font
score_msg = score_font.render("Score :",1,pygame.Color("green"))
score_msg_size = pygame.Color(0,0,0)
black = pygame.Color(0,0,0)


#for clock at the left corner
gameClock = pygame.time.Clock()

#we will define keys
def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            #FOR EXITE
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            
            #IF WE WANT TO CONTINUE PLAYING AGAIN
            elif event.key == pygame.K_y:
                return "yes"
            #if we dont want to play game
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)
def endGame():
    message = game_over_font.render("Game Over",1,pygame.Color("white"))
    message_play_again = play_again_font.render("Play Again ? (Y/N)",1,pygame.Color("green"))
    
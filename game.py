import pygame
from pygame.locals import *
import math

# initialise pygame
pygame.init()

# initialise clock
clock = pygame.time.Clock()
FPS = 69


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Velocity Rush')

# load bg image

bg = pygame.image.load('assets/bg.png').convert()
bg_width = bg.get_width()

#bg scrolling vars
bg_pos_x = 0
scroll_speed = 2 #adjustable
tiles = math.ceil( WINDOW_WIDTH / bg_width) + 1


running = True

while running:

    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #move the bg 
    bg_pos_x -= scroll_speed
    
    #check if it is out of screen, if yes then reset its position
    if bg_pos_x <= -bg_width:
         bg_pos_x = 0
         
    # # drawing the bg
    # for i in range (0, tiles):
    #     screen.blit(bg,(i * bg_width , 0))
        
    screen.blit(bg, (bg_pos_x,0))
    screen.blit(bg,(bg_pos_x+bg_width,0)) #second copy to fill the gap. we add the width to ensure that there is no gap
        
    pygame.display.update()
    
    
pygame.quit() 
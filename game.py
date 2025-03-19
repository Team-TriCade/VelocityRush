import pygame
from pygame.locals import *
# initialise pygame
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Velocity Rush')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0)) #the background color
    pygame.display.update()
    
    
pygame.quit() 
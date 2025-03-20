import pygame
from pygame.locals import *
import math 
import time

# initialise pygame
pygame.init()

# initialise clock
clock = pygame.time.Clock()
FPS = 69

#the last update time
last_update = 0

def interval(time_interval):
  global last_update
  current_time = time.time()
  if (current_time - last_update > time_interval):
      last_update = current_time
      return True
  return False
  

WINDOW_WIDTH = 900  # something less to prevent visual glitches while the bg is scrolling
WINDOW_HEIGHT = 768 # bg's height

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Velocity Rush')

# load bg image

bg = pygame.image.load('assets/bg.png').convert()
bg_width = bg.get_width()

# bg scrolling vars
bg_pos_x = 0
scroll_speed = 2
to_increment = 0.0069420
tiles = math.ceil( WINDOW_WIDTH / bg_width) + 1

# colors
GROUND_COLOR = (139,69,19) # rgb of brown color
GROUND_HEIGHT = 70 


running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # move the bg 
    bg_pos_x -= scroll_speed
    if(interval(2)): #increment it every 2 seconds
        scroll_speed = (scroll_speed + to_increment)
#    print(f'Scroll speed :- {scroll_speed}' )
    
    # check if it is out of screen, if yes then reset its position
    if bg_pos_x <= -bg_width:
        bg_pos_x += bg_width  
         
    # drawing the bg
    for i in range (0, tiles):
        screen.blit(bg,(i * bg_width , 0))


    screen.blit(bg, (bg_pos_x, 0))
    screen.blit(bg, (bg_pos_x + bg_width, 0))
    
    # draw the ground
    pygame.draw.rect(screen,GROUND_COLOR,(0, WINDOW_HEIGHT-GROUND_HEIGHT,WINDOW_WIDTH+1,GROUND_HEIGHT)) #(x coord, y coord, width, height)
    pygame.display.update()
    
    
pygame.quit() 
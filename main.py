import pygame
import sys
import os
from Functionality.skills import *
from Functionality.draw_graphics import *

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Archevale Idle Adventure")

screen.fill((0, 0, 0))
DrawSkills(screen=screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw all game elements here (e.g., skills, quests, monsters, locations)

    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)

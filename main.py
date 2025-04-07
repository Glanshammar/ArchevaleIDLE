import pygame
import sys
import os
from Functionality import *
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Archevale Idle Adventure")

player = Player()
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                xp_gain = 100
                player.woodcutting.gain_xp(xp_gain)
                print(f"Added {xp_gain} XP to Woodcutting! Current XP: {player.woodcutting.xp}")


    DrawBackground(screen=screen, background_path='Media/city1.jpeg')
    DrawSkills(screen=screen, player=player)
    pygame.display.update()
    clock.tick(60)
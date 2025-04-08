import pygame
from pygame import mixer
import sys
import os
from Functionality import *
from globals import *

pygame.init()
mixer.init()
mixer.music.load('/home/mondus/Music/music.mp3')
mixer.music.play(-1)

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Archevale Idle Adventure")

player = Player()
gamebg = GameBackground()
clock = pygame.time.Clock()

background = 'Media/city1.jpeg'

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
            if event.key == pygame.K_0:
                gamebg.set_background('shop')
            if event.key == pygame.K_1:
                gamebg.set_background('city')
        
        if gamebg.shop:
            background = 'Media/shop1.jpeg'
        if gamebg.city:
            background = 'Media/city1.jpeg'

    DrawBackground(screen=screen, background_path=background)
    DrawSkills(screen=screen, player=player)
    pygame.display.update()
    clock.tick(60)
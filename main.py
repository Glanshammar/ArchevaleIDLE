import pygame
from pygame import mixer
import pygame
import sys
from Functionality import *
from globals import *

pygame.init()
mixer.init()
# mixer.music.load('/home/mondus/Music/music.mp3')
# mixer.music.play(-1)

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Archevale Idle Adventure")

player = Player()
clock = pygame.time.Clock()

background = 'Media/city1.jpeg'
quit_button_rect = pygame.Rect(375, 425, 30, 30)

def Updates():
    DrawBackground(screen=screen, background_path=background)
    DrawSkills(screen=screen, player=player)
    pygame.draw.rect(screen, (255,0,0), quit_button_rect)
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                while player.woodcutting.level < 40:
                    player.woodcutting.ChopTree()
                    Updates()
            if event.key == pygame.K_5:
                player.woodcutting.ChopTree2()
            if event.key == pygame.K_1:
                gamebg.set_background('shop')
            if event.key == pygame.K_2:
                gamebg.set_background('city')
            if event.key == pygame.K_3:
                gamebg.set_background('forrest')
        
        if gamebg.city:
            background = 'Media/city1.jpeg'
        elif gamebg.shop:
            background = 'Media/shop1.jpeg'
        elif gamebg.forrest:
            background = 'Media/forrest.jpeg'

    
    Updates()
    clock.tick(60)
from .skills import *
import pygame

pygame.font.init()
font = pygame.font.Font(None, 28)
skills = [Woodcutting(), Fishing()]
woodcutting_icon = pygame.image.load('Media/tree.png')
fishing_icon = pygame.image.load('Media/fish.png')
woodcutting_icon = pygame.transform.scale(woodcutting_icon, (48, 48))
fishing_icon = pygame.transform.scale(fishing_icon, (48, 48))
skill_icons = {
    'Woodcutting': woodcutting_icon,
    'Fishing': fishing_icon
}

def DrawSkills(screen, player):
    skills = [player.woodcutting, player.fishing]
    for i, skill in enumerate(skills):
        icon = skill_icons.get(skill.name)
        icon_x = 10
        icon_y = 10 + i * 100
        text_x = icon_x + icon.get_width() + 10
        text_y = icon_y + (48 - font.get_height()) // 2
        screen.blit(icon, (icon_x, icon_y))
        level_text = font.render(f"Level {skill.level}", True, (255, 255, 255))
        xp_text = font.render(f"XP {int(skill.xp):,}", True, (255, 255, 255))
        screen.blit(level_text, (text_x, text_y))
        screen.blit(xp_text, (text_x, text_y + font.get_height() + 5))

def DrawBackground(screen, background_path):
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (1280, 720))
    screen.blit(background, (0, 0))

def DrawGraphic(screen, graphic_path, x, y):
    graphic = pygame.image.load(graphic_path)
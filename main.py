import pygame
import sys
import os
from skills import *

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Archevale Idle Adventure")

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game logic here (e.g., skills, quests, combat, travel)

    screen.fill((0, 0, 0))
    # Draw all game elements here (e.g., skills, quests, monsters, locations)
    for i, skill in enumerate(skills):
        # Get the icon for the current skill
        icon = skill_icons.get(skill.name)
        
        # Calculate positions for icon and text
        icon_x = 10
        icon_y = 10 + i * 100  # Adjusted to fit both icon and two lines of text vertically
        text_x = icon_x + icon.get_width() + 10  # Add a small gap between icon and text
        text_y = icon_y + (48 - font.get_height()) // 2  # Center the first line vertically
        
        # Draw the icon
        screen.blit(icon, (icon_x, icon_y))
        
        # Render and draw the text
        level_text = font.render(f"Level {skill.level}", True, (255, 255, 255))
        xp_text = font.render(f"XP {int(skill.xp):,}", True, (255, 255, 255))
        
        screen.blit(level_text, (text_x, text_y))
        screen.blit(xp_text, (text_x, text_y + font.get_height() + 5)) 

    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)

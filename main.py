# Imports
import pygame
import os

# Initialize pygame
pygame.init()

# Set up the window
WIDTH = 500
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = "Minesweeper"
pygame.display.set_caption(TITLE)
RESOURCES_FOLDER = "resources/"
ICON = pygame.image.load(os.path.join(RESOURCES_FOLDER, "icon.png"))
pygame.display.set_icon(ICON)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Window closed
            running = False  # Exit the game loop

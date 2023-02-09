# Imports
import pygame
import os

# Initialize pygame
pygame.init()

# Set up the window
WIDTH = 600
HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = "Minesweeper"
pygame.display.set_caption(TITLE)
IMAGES_FOLDER = "images/"
ICON = pygame.image.load(os.path.join(IMAGES_FOLDER, "icon.png"))
pygame.display.set_icon(ICON)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Other variables
ROWS = 20
COLS = 20
# In 'gamemodes' dictionary value is the number of bombs relative to the number of all tiles
gamemodes = {
    "Easy" : 0.1,
    "Medium" : 0.25,
    "Hard" : 0.5
}


# Game class
class Game:
    def __init__(self):
        pass


# Tile class
class Tile:
    def __init__(self):
        self.is_revealed = False


# Functions

# Function that displays the menu page
def draw_menu():
    # Display a bomb image
    bomb_img = pygame.image.load(os.path.join(IMAGES_FOLDER + "icon.png"))
    bomb_img = pygame.transform.scale(bomb_img, (256, 256))
    WINDOW.blit(bomb_img, ((WIDTH / 2) - (bomb_img.get_width() / 2), HEIGHT / 12.5))

    # Display a 'Minesweeper' heading
    heading_font = pygame.font.Font(pygame.font.get_default_font(), 50)
    heading_text = heading_font.render(TITLE, True, BLACK)
    WINDOW.blit(heading_text, ((WIDTH / 2) - (heading_text.get_width() / 2), HEIGHT / 2))

    # Display a 'Change difficulty' text
    difficulty_font = pygame.font.Font(pygame.font.get_default_font(), 30)
    difficulty_text = difficulty_font.render("Change difficulty:", True, BLACK)
    WINDOW.blit(difficulty_text, ((WIDTH / 2) - (difficulty_text.get_width() / 2), HEIGHT / 2 + (heading_text.get_height() * 1.5)))

# Game loop
running = True
while running:
    # Make the background white
    WINDOW.fill(WHITE)

    # Check user events (keyboard, mouse etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Window closed
            running = False  # Exit the game loop


    draw_menu()

    # Update the window
    pygame.display.flip()

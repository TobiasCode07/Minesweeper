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
GAMES_FOLDER = "games/"
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
GAMEMODES = {
    "Easy": 0.1,
    "Medium": 0.25,
    "Hard": 0.5
}
# Current difficulty is the first one when starting ('Easy')
CURRENT_DIFF = 0


# Game class
class Game:
    def __init__(self):
        pass


# Tile class
class Tile:
    def __init__(self):
        self.is_revealed = False


# Functions
# Function that checks if there is a game saved
def is_game(difficulty):
    # Check if file is empty
    if os.stat(os.path.join(GAMES_FOLDER, f"{difficulty}.txt")).st_size == 0:
        return False

    return True


# Function that displays the menu page
def draw_menu():
    # Display a bomb image
    bomb_img = pygame.image.load(os.path.join(IMAGES_FOLDER + "icon.png"))
    bomb_img = pygame.transform.scale(bomb_img, (256, 256))
    WINDOW.blit(bomb_img, ((WIDTH / 2) - (bomb_img.get_width() / 2), 50))

    # Display a 'Minesweeper' heading
    heading_font = pygame.font.Font(pygame.font.get_default_font(), 50)
    heading_text = heading_font.render(TITLE, True, BLACK)
    WINDOW.blit(heading_text, ((WIDTH / 2) - (heading_text.get_width() / 2), 325))

    # Display a 'Change difficulty' text
    difficulty_font = pygame.font.Font(pygame.font.get_default_font(), 30)
    difficulty_text = difficulty_font.render("Change difficulty:", True, BLACK)
    WINDOW.blit(difficulty_text, ((WIDTH / 2) - (difficulty_text.get_width() / 2), 420))

    # Display the current difficulty chosen
    current_diff_font = pygame.font.Font(pygame.font.get_default_font(), 40)
    current_diff_text = current_diff_font.render(list(GAMEMODES.keys())[CURRENT_DIFF], True, BLACK)
    WINDOW.blit(current_diff_text, ((WIDTH / 2) - (current_diff_text.get_width() / 2), 500))

    # Display arrows to change the difficulty
    global decrease_diff, increase_diff
    arrow_font = pygame.font.Font(pygame.font.get_default_font(), 60)

    if CURRENT_DIFF > 0:
        decrease_diff = pygame.draw.circle(WINDOW, GRAY, (150, 500 + 15), 30)
        left_arrow = arrow_font.render("<", True, BLACK)
        WINDOW.blit(left_arrow, (decrease_diff.x + 10, decrease_diff.y - 2.5))

    if CURRENT_DIFF < 2:
        increase_diff = pygame.draw.circle(WINDOW, GRAY, (450, 500 + 15), 30)
        right_arrow = arrow_font.render(">", True, BLACK)
        WINDOW.blit(right_arrow, (increase_diff.x + (right_arrow.get_width() / 2), increase_diff.y - 2.5))

    # Display 'New Game' and 'Resume Game' buttons
    game_btn_font = pygame.font.Font(pygame.font.get_default_font(), 30)
    game_btn_width = 225
    game_btn_height = 60
    if is_game(list(GAMEMODES.keys())[CURRENT_DIFF]):
        new_game_rect = pygame.draw.rect(WINDOW, GRAY, pygame.Rect(50, 600, game_btn_width, game_btn_height))
        resume_game_rect = pygame.draw.rect(WINDOW, GRAY, pygame.Rect(325, 600, game_btn_width, game_btn_height))

        new_game_text = game_btn_font.render("New Game", True, BLACK)
        WINDOW.blit(new_game_text, (new_game_rect.x + (game_btn_width / 2) - (new_game_text.get_width() / 2),
                                    new_game_rect.y + (game_btn_height / 2) - (new_game_text.get_height() / 2)))

        resume_game_text = game_btn_font.render("Resume Game", True, BLACK)
        WINDOW.blit(resume_game_text, (resume_game_rect.x + (game_btn_width / 2) - (resume_game_text.get_width() / 2),
                                    resume_game_rect.y + (game_btn_height / 2) - (resume_game_text.get_height() / 2)))
    else:
        new_game_rect = pygame.draw.rect(WINDOW, GRAY, pygame.Rect(WIDTH / 2 - (game_btn_width / 2),
                                                                   600, game_btn_width, game_btn_height))
        new_game_text = game_btn_font.render("New Game", True, BLACK)
        WINDOW.blit(new_game_text, (new_game_rect.x + (game_btn_width / 2) - (new_game_text.get_width() / 2),
                                    new_game_rect.y + (game_btn_height / 2) - (new_game_text.get_height() / 2)))

# Game loop
running = True
while running:
    # Make the background white
    WINDOW.fill(WHITE)

    # Check user events (keyboard, mouse etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Window closed
            running = False  # Exit the game loop

        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if decrease or increase difficulty buttons were clicked
            if CURRENT_DIFF > 0:
                if decrease_diff.collidepoint(event.pos):
                    CURRENT_DIFF -= 1

            if CURRENT_DIFF < 2:
                if increase_diff.collidepoint(event.pos):
                    CURRENT_DIFF += 1

    draw_menu()

    # Update the window
    pygame.display.flip()

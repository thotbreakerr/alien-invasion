import sys      # exits the game when the players quits
import pygame   # Contains functionality needed to make a game

from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")    # Window title

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:

        # Watch for key board and mouse events.
        # poll for events
        # pygame.QUIT means the user clicked X to close your window
        # Im assuming all the code to move around will be in this for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)   # Generates background first
        ship.blit()     # Generates ship onto screen after background

        # Make the most recently drawn screen visible
        # flip() the display to put your work on screen
        pygame.display.flip() 

run_game()
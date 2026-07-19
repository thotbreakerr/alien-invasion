import sys      # exits the game when the players quits
import pygame   # Contains functionality needed to make a game
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")    # Window title

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make an alien
    alien = Alien(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game. If anything happens in game look at loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)   # Keyboard response/player input
        ship.update()   # Update position of ship
        gf.update_bullets(bullets)  # Any bullets that have been fired
        gf.update_screen(ai_settings, screen, ship, alien, bullets)    # Use updated positions to draw a new screen

run_game()
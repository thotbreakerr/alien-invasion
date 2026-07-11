import pygame

class Ship():
    """Initialize the ship and set its starting position."""
    def __init__(self, screen):
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()    # Stores the screens rect (1200, 800)

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx    # Places ship in middle
        self.rect.bottom = self.screen_rect.bottom      # Places ship at the bottom

    def blit(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
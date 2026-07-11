import sys      # exits the game when the players quits
import pygame   # Contains functionality needed to make a game

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")    # Window title

    # Start the main loop for the game.
    while True:

        # Watch for key board and mouse events.
        # poll for events
        # pygame.QUIT means the user clicked X to close your window
        # Im assuming all the code to move around will be in this for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        

        # Make the most recently drawn screen visible
        # flip() the display to put your work on screen
        pygame.display.flip() 

run_game()
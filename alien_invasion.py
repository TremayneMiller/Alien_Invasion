import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game, settingg, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make alien.
    # alien = Alien(ai_settings, screen)
    print (pygame.image.get_extended())

    # Set the background color
    # bg_color = (230, 230, 230)

    # Make ship, a group for the bullets, and a group for the aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Create a fleet of the aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    clock = pygame.time.Clock()
    # Start the loop for the game.
    while True:
        # Watch for keyboard and mouse movements.
        """refactored. Original function commented out(below) and moved to game functions module"""
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        clock.tick(30)


        # # Redraw the screen during each pass through the loop.
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        #
        # # Make the most recently drawn screen visible.
        # pygame.display.flip()

run_game()

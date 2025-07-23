"""
Python-Blackjack - Version française 1.0

Copyright © Gaëtan Sencie 2024
Tous droits réservés.
"""

import os
import sys
import pygame
import random
import json # Pour la gestion du Hall of Fame

# Initialiser Pygame
pygame.init()

# Dimensions de l'écran
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
BLUE = (0, 0, 255)

# Créer l'écran (initialisé après la splash screen pour la fenêtre principale)
screen = None # Sera initialisé après la splash screen
pygame.display.set_caption("Blackjack")



CODE SOUS LICENCE




if __name__ == '__main__':
    main()
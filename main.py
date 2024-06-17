import pygame
import sys


# Ініціалізація Pygame
pygame.init()

# Налаштування
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 20, 20
MINE_COUNT = 40
TILE_SIZE = WIDTH // COLS

# Вікно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")


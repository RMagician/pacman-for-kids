# maze.py
import pygame
from config import WHITE


class Maze:
    def __init__(self):
        self.walls = [
            pygame.Rect(50, 50, 350, 20),
            pygame.Rect(50, 50, 20, 400),
            pygame.Rect(50, 430, 350, 20),
            pygame.Rect(430, 50, 20, 400),
            pygame.Rect(150, 150, 150, 20),
            pygame.Rect(150, 250, 20, 200),
            pygame.Rect(250, 350, 150, 20),
            pygame.Rect(350, 150, 20, 200),
            pygame.Rect(100, 100, 20, 200),
            pygame.Rect(200, 100, 150, 20),
            pygame.Rect(300, 200, 20, 200),
        ]

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, WHITE, wall)

import pygame
from config import WIDTH, HEIGHT, YELLOW
from maze import Maze


class Player:
    def __init__(self, maze: Maze):
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.maze: Maze = maze

    def handle_input(self):
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y

        if keys[pygame.K_LEFT]:
            new_x -= self.speed
        if keys[pygame.K_RIGHT]:
            new_x += self.speed
        if keys[pygame.K_UP]:
            new_y -= self.speed
        if keys[pygame.K_DOWN]:
            new_y += self.speed

        new_rect = pygame.Rect(new_x, new_y, 20, 20)
        if not self.collides_with_walls(new_rect):
            self.x, self.y = new_x, new_y
            self.rect.topleft = (self.x, self.y)

    def collides_with_walls(self, new_rect):
        for wall in self.maze.walls:
            if new_rect.colliderect(wall):
                return True
        return False

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)

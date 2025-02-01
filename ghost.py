import pygame
import random
from config import WIDTH, HEIGHT, RED, WHITE
from maze import Maze


class Ghost:
    def __init__(self, x, y, maze):
        self.maze = maze
        self.speed = 2
        self.direction = random.choice(
            [(1, 0), (-1, 0), (0, 1), (0, -1)]
        )  # Random initial direction
        self.x, self.y = self.find_valid_position(x, y)
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

    def find_valid_position(self, x, y):
        # If the initial position collides, find the nearest open space
        temp_rect = pygame.Rect(x, y, 20, 20)
        if not self.collides_with_walls(temp_rect):
            return x, y

        for dx in range(-40, 41, 10):  # Search nearby in a 40-pixel radius
            for dy in range(-40, 41, 10):
                new_x, new_y = x + dx, y + dy
                temp_rect = pygame.Rect(new_x, new_y, 20, 20)
                if not self.collides_with_walls(temp_rect):
                    return new_x, new_y

        return WIDTH // 2, HEIGHT // 2  # Default to center if no valid position found

    def update(self, player, game):
        new_x = self.x + self.direction[0] * self.speed
        new_y = self.y + self.direction[1] * self.speed
        new_rect = pygame.Rect(new_x, new_y, 20, 20)

        if not self.collides_with_walls(new_rect):
            self.x, self.y = new_x, new_y
        else:
            self.change_direction()

        self.rect.topleft = (self.x, self.y)

        # Check for collision with the player
        if self.rect.colliderect(player.rect):
            game.game_over()

    def collides_with_walls(self, new_rect):
        for wall in self.maze.walls:
            if new_rect.colliderect(wall):
                return True
        return False

    def change_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for direction in directions:
            new_x = self.x + direction[0] * self.speed
            new_y = self.y + direction[1] * self.speed
            new_rect = pygame.Rect(new_x, new_y, 20, 20)
            if not self.collides_with_walls(new_rect):
                self.direction = direction
                break

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

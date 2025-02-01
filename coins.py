import pygame
import random
import time
from config import WIDTH, HEIGHT, YELLOW


class Coin:
    def __init__(self, maze, num_coins=10):
        self.maze = maze
        self.num_coins = num_coins
        self.coins = []
        self.respawn_timers = {}
        self.open_spaces = self.find_open_spaces()
        self.generate_coins()
        self.score = 0  # Initialize score counter

    def find_open_spaces(self):
        open_spaces = []
        for x in range(20, WIDTH - 20, 20):
            for y in range(20, HEIGHT - 20, 20):
                coin_rect = pygame.Rect(x, y, 10, 10)
                if not any(wall.colliderect(coin_rect) for wall in self.maze.walls):
                    open_spaces.append((x, y))
        return open_spaces

    def generate_coins(self):
        for _ in range(self.num_coins):
            self.spawn_coin()

    def spawn_coin(self):
        if not self.open_spaces:
            return
        x, y = random.choice(self.open_spaces)
        coin_rect = pygame.Rect(x, y, 10, 10)
        self.coins.append(coin_rect)

    def draw(self, screen):
        for coin in self.coins:
            pygame.draw.circle(screen, YELLOW, (coin.x + 5, coin.y + 5), 5)

        # Display the score on the screen
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, YELLOW)
        screen.blit(score_text, (10, 40))

    def check_collision(self, player):
        for coin in self.coins[:]:
            if player.rect.colliderect(coin):
                self.coins.remove(coin)
                self.respawn_timers[time.time() + random.randint(1, 5)] = (
                    None  # Store respawn time
                )
                self.score += 1  # Increase score when a coin is collected

    def regenerate_coins(self):
        current_time = time.time()
        to_respawn = [t for t in self.respawn_timers if current_time >= t]

        for t in to_respawn:
            self.spawn_coin()
            del self.respawn_timers[t]

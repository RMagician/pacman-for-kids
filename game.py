import pygame
import time
from config import WIDTH, HEIGHT, BLACK, WHITE
from player import Player
from ghost import Ghost
from maze import Maze
from coins import Coin


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over_flag = False
        self.start_time = time.time()  # Track game start time

        self.maze = Maze()
        self.player = Player(self.maze)
        self.ghosts = [
            Ghost(200, 200, self.maze),
            Ghost(100, 100, self.maze),
            Ghost(300, 300, self.maze),
        ]
        self.coins = Coin(self.maze, num_coins=5)  # Initialize coins

    def game_over(self):
        if time.time() - self.start_time >= 10:  # 10-second grace period
            self.game_over_flag = True

    def restart_game(self):
        self.__init__()  # Reset the game state

    def draw_game_over_screen(self):
        font = pygame.font.Font(None, 50)
        text = font.render("Game Over! Press R to Restart", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.fill(BLACK)
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def draw_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Survived: {elapsed_time} sec", True, WHITE)
        self.screen.blit(timer_text, (10, 10))

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.coins.score}", True, WHITE)
        self.screen.blit(score_text, (10, 40))

    def run(self):
        while self.running:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if (
                    self.game_over_flag
                    and event.type == pygame.KEYDOWN
                    and event.key == pygame.K_r
                ):
                    self.restart_game()

            if not self.game_over_flag:
                self.player.handle_input()
                self.player.update()

                for ghost in self.ghosts:
                    ghost.update(self.player, self)
                    ghost.draw(self.screen)

                self.coins.check_collision(
                    self.player
                )  # Check if player collects coins
                self.coins.regenerate_coins()  # Regenerate coins when necessary

                self.maze.draw(self.screen)
                self.coins.draw(self.screen)  # Draw coins on screen
                self.player.draw(self.screen)
                self.draw_timer()
                self.draw_score()  # Draw the score on screen
            else:
                self.draw_game_over_screen()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 800
GRID_SIZE = 50
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 255, 0)

# Directional constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid_size = GRID_SIZE
        self.fps = FPS

        # Initialize Pygame screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        # Initialize game variables
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.generate_food()
        self.direction = RIGHT

        # Set up the clock to control the frame rate
        self.clock = pygame.time.Clock()

    def generate_food(self):
        while True:
            food = (random.randint(0, self.width - self.grid_size) // self.grid_size * self.grid_size,
                    random.randint(0, self.height - self.grid_size) // self.grid_size * self.grid_size)
            if food not in self.snake:
                return food

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, WHITE, (segment[0], segment[1], self.grid_size, self.grid_size))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], self.grid_size, self.grid_size))

    def move_snake(self):
        head = (self.snake[0][0] + self.direction[0] * self.grid_size, self.snake[0][1] + self.direction[1] * self.grid_size)
        self.snake.insert(0, head)

        # Check for collision with food
        if head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()

        # Check for collision with walls or itself
        if (head[0] < 0 or head[0] >= self.width or
            head[1] < 0 or head[1] >= self.height or
            head in self.snake[1:]):
            self.game_over()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

    def game_over(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            self.handle_input()
            self.move_snake()

            # Draw background
            self.screen.fill(BLACK)

            # Draw snake and food
            self.draw_snake()
            self.draw_food()

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(self.fps)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()

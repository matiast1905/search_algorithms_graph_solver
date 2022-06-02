from enum import Enum, auto
import pygame
import sys

from constants import BLACK, ORANGE, WINDOWS_HEIGHT, WINDOWS_WIDTH, WHITE, GRAY, SQUARE_SIZE, LIME
from src.grid import Grid

class SquareColors(Enum):
    ORANGE = auto()
    LIME = auto()
    BLACK = auto()

class Screen:
    """Class to handle the pygame windows"""
    def __init__(self, caption: str, grid: Grid) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
        pygame.display.set_caption(caption)
        self.grid = grid
        self.bg_color = WHITE
        self.grid_color = GRAY
    
    def run(self) -> None:
        """
        Start the main loop for renderizing the grid
        """
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self) -> None:
        """
        Watch for keyboard and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                grid_indexes = self.grid.get_grid_indexes(pygame.mouse.get_pos())
                self.grid.user_selected_squares.append(grid_indexes)
    
    def _fill_squares(self) -> None:
        """Paint the squares selected by the user"""
        for pos,square in enumerate(self.grid.user_selected_squares, start = 1):
            x_min = square[0] * SQUARE_SIZE
            y_min = square[1] * SQUARE_SIZE
            rect = pygame.Rect(x_min, y_min, SQUARE_SIZE, SQUARE_SIZE)
            # Select the color according to the position of the square in the list (first : start, second : end, all the rest are walls)
            color = SquareColors(min(len(SquareColors), pos)).name
            pygame.draw.rect(self.screen, color ,rect)
    
    def _update_screen(self) -> None:
        """
        Redraw screen during each pass of the game loop
        """
        # Insert background color
        self.screen.fill(self.bg_color)
        # Draw the grid
        self._draw_grid()
        # Paint the squares selected by the user
        self._fill_squares()
        # Make the most recently drawn screen visible
        pygame.display.flip()
        
    def _draw_grid(self) -> None:
        for x in range(0, WINDOWS_WIDTH, SQUARE_SIZE):
            for y in range(0, WINDOWS_HEIGHT, SQUARE_SIZE):
                rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)

if __name__ == "__main__":
    screen = Screen("Maze Solver", Grid(10,10))
    screen.run()

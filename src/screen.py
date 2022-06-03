import sys
from typing import Tuple

import pygame

from constants import SQUARE_SIZE, Cell, GRAY
from grid import Grid

class Screen:
    """Class to handle the pygame windows"""

    def __init__(self, caption: str, grid: Grid, solve_method: str, square_size: int, grid_color: Tuple[int, int, int]) -> None:
        pygame.init()
        self.grid = grid
        self.square_size = square_size
        self.windows_width = self.square_size * self.grid.n_rows
        self.windows_height = self.square_size * self.grid.n_cols
        self.screen = pygame.display.set_mode(
            (self.windows_width, self.windows_height))
        pygame.display.set_caption(caption)
        self.bg_color = Cell.EMPTY.value
        self.grid_color = grid_color
        self.solve_method = solve_method
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        """
        Start the main loop for renderizing the grid
        """
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(100)

    def _check_events(self) -> None:
        """
        Watch for keyboard and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if any(pygame.mouse.get_pressed()):
            if pygame.mouse.get_pressed()[0]:
                self.grid.fill_grid(pygame.mouse.get_pos())
            elif pygame.mouse.get_pressed()[1]:
                self.grid.delete_grid_value(pygame.mouse.get_pos())
            elif pygame.mouse.get_pressed()[2]:
                self.grid.solve(self.solve_method)

    def _fill_squares(self) -> None:
        """Paint the squares selected by the user"""
        for row_num, row in enumerate(self.grid.grid):
            for col_num, value in enumerate(row):
                x_min = row_num * self.square_size
                y_min = col_num * self.square_size
                rect = pygame.Rect(
                    x_min, y_min, self.square_size, self.square_size)
                color = value
                pygame.draw.rect(self.screen, color, rect)

    def _update_screen(self) -> None:
        """
        Redraw screen during each pass of the game loop
        """
        # Insert background color
        self.screen.fill(self.bg_color)
        # Paint the squares selected by the user
        self._fill_squares()
        # Draw the grid
        self._draw_mesh()
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _draw_mesh(self) -> None:
        """Draw the mesh in the screen on top of the squares"""
        for x in range(0, self.windows_width, self.square_size):
            for y in range(0, self.windows_height, self.square_size):
                rect = pygame.Rect(x, y, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)


if __name__ == "__main__":
    screen = Screen("Maze Solver", Grid(50, 50),"BFS", SQUARE_SIZE, GRAY)
    screen.run()

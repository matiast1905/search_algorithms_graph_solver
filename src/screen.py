import sys
from typing import Optional

import pygame

from constants import Cell



class Screen:
    """Class to handle the pygame windows"""

    def __init__(
        self, caption: str, square_size: int, n_rows: int, n_cols: int, bg_color: Cell, grid_color: Cell
    ) -> None:
        pygame.init()
        self.square_size = square_size
        self.windows_width = self.square_size * n_rows
        self.windows_height = self.square_size * n_cols
        self.screen = pygame.display.set_mode((self.windows_width, self.windows_height))
        pygame.display.set_caption(caption)
        self.bg_color = bg_color
        self.grid_color = grid_color
        self.clock = pygame.time.Clock()

    def check_events(self) -> Optional [tuple[tuple[int,int,int], tuple[int, int]]]:
        """
        Watch for keyboard and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if any(pygame.mouse.get_pressed()):
            return pygame.mouse.get_pressed(), pygame.mouse.get_pos()
        return None

    def update_screen(self, grid, framerate = 60) -> None:
        """
        Redraw screen during each pass of the game loop
        """
        self.screen.fill(self.bg_color)
        self._fill_squares(grid)
        self._draw_mesh()
        pygame.display.flip()
        self.clock.tick(framerate)

    def _fill_squares(self, grid) -> None:
        """Paint the squares selected by the user"""
        for row_num, row in enumerate(grid):
            for col_num, color in enumerate(row):
                x_min = row_num * self.square_size
                y_min = col_num * self.square_size
                rect = pygame.Rect(x_min, y_min, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, color, rect)

    def _draw_mesh(self) -> None:
        """Draw the mesh in the screen on top of the squares"""
        for x in range(0, self.windows_width, self.square_size):
            for y in range(0, self.windows_height, self.square_size):
                rect = pygame.Rect(x, y, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)

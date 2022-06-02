from enum import Enum
from typing import List, NamedTuple, Tuple

from constants import SQUARE_SIZE, Cell

class GridLocation(NamedTuple):
    row: int
    column: int


class Grid:
    """
    Class to manage the grid.
    """
    def __init__(self, rows: int, cols: int) -> None:
        self.n_rows = rows
        self.n_cols = cols    
        self.grid: List[List[Cell]] = [[Cell.EMPTY.value for _ in range(cols)] for _ in range(rows)]
        self.fill_counter = 0

    def fill_grid(self, pos : Tuple[int, int]) -> None:
        """Fill the grid with the appropiate value"""
        grid_loc = GridLocation(pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE)
        if self.fill_counter == 0:
            self.grid[grid_loc.row][grid_loc.column] = Cell.START.value
        if self.fill_counter == 1:
            self.grid[grid_loc.row][grid_loc.column] = Cell.GOAL.value
        if self.fill_counter > 1:
            self.grid[grid_loc.row][grid_loc.column] = Cell.WALL.value
        self.fill_counter += 1
        

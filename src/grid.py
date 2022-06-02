from typing import List, Tuple

from constants import SQUARE_SIZE


class Grid:
    """
    Class to manage the grid.
    """
    def __init__(self, rows: int, cols: int ) -> None:        
        self.grid: List[List[str]] = [[" " for _ in range(cols)] for _ in range(rows)]
        self.user_selected_squares : List[Tuple[int, int]] = []

    @staticmethod
    def get_grid_indexes(pos : Tuple[int, int]) -> Tuple[int, int]:
        """Return the grid indexes for a certain position of the mouse in the screen"""
        return pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE

from enum import Enum
from typing import List, NamedTuple, Tuple

from constants import SQUARE_SIZE, Cell
from generic_search import bfs, node_to_path

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
        # counter is neccesary to know which type of cell are we handling(ie: START, GOAL, WALL, etc.)
        self.fill_counter = 0

    def fill_grid(self, pos : Tuple[int, int]) -> None:
        """Fill the grid with the appropiate value"""
        grid_loc = GridLocation(pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE)
        if self.fill_counter == 0:
            self.grid[grid_loc.row][grid_loc.column] = Cell.START.value
            self.start: GridLocation = grid_loc
        if self.fill_counter == 1:
            self.grid[grid_loc.row][grid_loc.column] = Cell.GOAL.value
            self.goal: GridLocation = grid_loc
        if self.fill_counter > 1:
            self.grid[grid_loc.row][grid_loc.column] = Cell.WALL.value
        self.fill_counter += 1
    
    def goal_test(self, gl: GridLocation) -> bool:
        return gl == self.goal

    def successors(self, gl: GridLocation) -> List[GridLocation]:
        locations: List[GridLocation] = []
        if gl.row + 1 < self.n_rows and self.grid[gl.row + 1][gl.column] != Cell.WALL.value:
            locations.append(GridLocation(gl.row + 1, gl.column))
        if gl.row - 1 >= 0 and self.grid[gl.row - 1][gl.column] != Cell.WALL.value:
            locations.append(GridLocation(gl.row - 1, gl.column))
        if gl.column + 1 < self.n_cols and self.grid[gl.row][gl.column + 1] != Cell.WALL.value:
            locations.append(GridLocation(gl.row, gl.column + 1))
        if gl.column - 1 >= 0 and self.grid[gl.row][gl.column - 1] != Cell.WALL.value:
            locations.append(GridLocation(gl.row, gl.column - 1))
        return locations

    def mark(self, path: List[GridLocation]):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.PATH.value
        self.grid[self.start.row][self.start.column] = Cell.START.value
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL.value
    
    def solve(self):
        # Test BFS
        solution = bfs(self.start, self.goal_test, self.successors, True)
        if solution is None:
            print("No solution found using breadth-first search!")
        else:
            path = node_to_path(solution[0])
            print(f"Solution using breadth-first search!: {len(path)} steps and {solution[1]} iterations",end = "\n\n")
            self.mark(path)
            

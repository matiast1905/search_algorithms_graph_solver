from enum import Enum
from typing import List, NamedTuple, Tuple
from time import time

from constants import SQUARE_SIZE, Cell
from generic_search import T, Node, Queue, bfs, dfs, node_to_path


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
        self.grid: List[List[Cell]] = [
            [Cell.EMPTY.value for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.goal = None

    def fill_grid(self, pos: Tuple[int, int]) -> None:
        """Fill the grid with the appropiate value"""
        grid_loc = GridLocation(pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE)
        if not self.start:
            self.grid[grid_loc.row][grid_loc.column] = Cell.START.value
            self.start = grid_loc
        elif not self.goal and grid_loc != self.start:
            self.grid[grid_loc.row][grid_loc.column] = Cell.GOAL.value
            self.goal = grid_loc
        elif grid_loc != self.start and grid_loc != self.goal:
            self.grid[grid_loc.row][grid_loc.column] = Cell.WALL.value

    def delete_grid_value(self, pos: Tuple[int, int]) -> None:
        """Remove the value from the grid and leave an empty space"""
        grid_loc = GridLocation(pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE)
        self.grid[grid_loc.row][grid_loc.column] = Cell.EMPTY.value
        if grid_loc == self.start:
            self.start = None
        elif grid_loc == self.goal:
            self.goal = None

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

    def mark(self, path: List[GridLocation], final_solution: bool =False):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.PATH.value if not final_solution else Cell.FINAL_PATH.value
        self.grid[self.start.row][self.start.column] = Cell.START.value
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL.value

    def solve(self, method="BFS"):
        if method == "BFS":
            solution, explored_nodes = bfs(
                self.start, self.goal_test, self.successors)
        elif method == "DFS":
            solution, explored_nodes = dfs(
                self.start, self.goal_test, self.successors)
        if solution is None:
            print("No solution found using breadth-first search!")
        else:
            return solution, explored_nodes

from typing import List, NamedTuple, Optional
import random
from constants import Cell


class GridLocation(NamedTuple):
    row: int
    column: int


class Grid:
    """
    Class to create and update the grid.
    """

    def __init__(self, rows: int, cols: int) -> None:
        self.n_rows: int = rows
        self.n_cols: int = cols
        self.grid: list[list[Cell]] = [
            [Cell.EMPTY.value] * cols for _ in range(rows)]
        self.start: Optional[GridLocation] = None
        self.goal: Optional[GridLocation] = None

    def set_grid_value(self, grid_loc: GridLocation) -> None:
        """Fill the grid with the appropiate value"""
        if not self.start:
            self.grid[grid_loc.row][grid_loc.column] = Cell.START.value
            self.start = grid_loc
        elif not self.goal and grid_loc != self.start:
            self.grid[grid_loc.row][grid_loc.column] = Cell.GOAL.value
            self.goal = grid_loc
        elif grid_loc != self.start and grid_loc != self.goal:
            self.grid[grid_loc.row][grid_loc.column] = Cell.WALL.value
    
    def random_grid_fill(self, sparseness = 0.3):
        for i,row in enumerate(self.grid):
            for j,_ in enumerate(row):
                self.grid[i][j] = Cell.WALL.value if random.random() < sparseness else Cell.EMPTY.value

    def empty_cell(self, grid_loc: GridLocation) -> None:
        """Remove the value from the grid and leave an empty space"""
        self.grid[grid_loc.row][grid_loc.column] = Cell.EMPTY.value
        if grid_loc == self.start:
            self.start = None
        elif grid_loc == self.goal:
            self.goal = None

    def goal_test(self, gl: GridLocation) -> bool:
        """Check if a value of a grid is the goal"""
        return gl == self.goal

    def successors(self, gl: GridLocation) -> List[GridLocation]:
        locations: List[GridLocation] = []
        if gl.row + 1 < self.n_rows and self.grid[gl.row + 1][gl.column] != Cell.WALL.value:
            locations.append(GridLocation(gl.row + 1, gl.column)) # Right
        if gl.row - 1 >= 0 and self.grid[gl.row - 1][gl.column] != Cell.WALL.value:
            locations.append(GridLocation(gl.row - 1, gl.column)) # Left
        if gl.column + 1 < self.n_cols and self.grid[gl.row][gl.column + 1] != Cell.WALL.value:
            locations.append(GridLocation(gl.row, gl.column + 1)) # Down
        if gl.column - 1 >= 0 and self.grid[gl.row][gl.column - 1] != Cell.WALL.value:
            locations.append(GridLocation(gl.row, gl.column - 1)) # Up
        return locations

    def mark(self, path: List[GridLocation], final_solution: bool =False):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.PATH.value if not final_solution else Cell.FINAL_PATH.value
        self.grid[self.start.row][self.start.column] = Cell.START.value
        self.grid[self.goal.row][self.goal.column] = Cell.GOAL.value

    # def solve(self, method="BFS"):
    #     if method == "BFS":
    #         solution = bfs(
    #             self.start, self.goal_test, self.successors)
    #     elif method == "DFS":
    #         solution = dfs(
    #             self.start, self.goal_test, self.successors)
    #     if not solution:
    #         print("No solution found using breadth-first search!")
    #     else:
    #         return solution, explored_nodes

from screen import Screen
from grid import Grid, GridLocation
from constants import GRAY, SQUARE_SIZE, WHITE
from solver import Solver
from solver_utils import node_to_path


class MazeSolver:
    def __init__(self, grid: Grid, screen: Screen, solver : Solver) -> None:
        self.grid = grid
        self.screen = screen
        self.solver = solver

    def run(self) -> None:
        """
        Main loop for renderizing the grid
        """
        while True:
            events = self.screen.check_events()
            if events:
                mouse_button_pressed, mouse_position = events
                if mouse_button_pressed[0]:
                    self.grid.set_grid_value(self._get_grid_position(mouse_position))
                elif mouse_button_pressed[1]:
                    self.grid.empty_cell(self._get_grid_position(mouse_position))
                elif mouse_button_pressed[2]:
                    self.solve_maze()
            self.screen.update_screen(self.grid.grid)

    def _get_grid_position(self, mouse_position) -> GridLocation:
        """Return grid position coordinates from a mouse position in the screen"""
        return GridLocation(mouse_position[0] // self.screen.square_size, mouse_position[1] // self.screen.square_size)
    
    def solve_maze(self):
        solver.set_solver_params(self.grid.start)
        while not self.solver.solved:
            self.screen.check_events()
            node = self.solver.search_next_node()
            path = node_to_path(node)
            self.grid.mark(path, self.solver.solved)
            self.screen.update_screen(self.grid.grid, 80)


if __name__ == "__main__":
    grid = Grid(30, 30)
    grid.random_grid_fill()
    screen = Screen("Maze solver", SQUARE_SIZE, grid.n_rows, grid.n_cols, WHITE, GRAY)
    solver = Solver("bfs", grid.goal_test, grid.successors)
    maze_solver = MazeSolver(grid, screen, solver)
    maze_solver.run()

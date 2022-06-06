from typing import Callable
from solver_utils import T, Node, Stack, Queue, PriorityQueue


container = {
    "dfs" : Stack(),
    "bfs" : Queue(),
    "astar" : PriorityQueue() # Not implemented yet
}

class Solver:
    """Class to create a solver for the maze"""
    def __init__(self, solver_type : str, goal_test: Callable[[T], bool], successors: Callable[[T], list[T]]):
        self.goal_test = goal_test
        self.successors = successors
        self.solved = False
        self.frontier = container.get(solver_type.lower(), None)
    
    def set_solver_params(self, start):
        """Set the solver parameters with a starting point"""
        self.explored = {start}
        self.frontier.push(Node(start, None))
    
    def search_next_node(self) -> Node[T]:
        """Explores the next node of the container and returns a Node object"""
        if self.frontier.empty:
            # Not solution for the maze
            print("The maze does not have a solution")
        current_node: Node[T] = self.frontier.pop()
        current_state: T = current_node.state
        # if we found the goal, we're done
        if self.goal_test(current_state):
            self.solved = True
            return current_node
        # check where we can go next and haven't explored
        for child in self.successors(current_state):
            if child in self.explored:  # skip children we already explored
                continue
            self.explored.add(child)
            self.frontier.push(Node(child, current_node))
        return current_node

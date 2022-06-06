
#----------------------------COLORS------------------------------------------------------
from enum import Enum
from typing import Literal


BLACK = (0, 0, 0)
WHITE = (245, 245, 245)
GRAY = (100, 100, 100)
ORANGE = (255,69,0)
LIME = (0,255,0)
BLUE = (0, 102, 153)
VIOLET = (190, 0, 219)

#----------------------------GRID COLORS-------------------------------------------------
class Cell(Enum):
    EMPTY = WHITE
    WALL = BLACK
    START = ORANGE
    GOAL = LIME
    PATH = BLUE
    FINAL_PATH = VIOLET

#----------------------------PYGAME WINDOWS----------------------------------------------
ROWS = COLS = 40
SQUARE_SIZE = 20
WINDOWS_WIDTH = WINDOWS_HEIGHT = ROWS * SQUARE_SIZE

#----------------------------MAZE--------------------------------------------------------
RANDOM_MAZE_SPARSENESS = 0.5

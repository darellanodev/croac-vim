from src.exceptions import BoardIndexError


class Board:
    def __init__(self, layout):
        self.grid = [list(line) for line in layout]

    def _check_bounds(self, x, y):
        if x < 0 or y < 0:
            raise BoardIndexError("x and y positions must be zero or greater")
        if y >= len(self.grid):
            raise BoardIndexError("y position is out of range")
        if x >= len(self.grid[y]):
            raise BoardIndexError("x position is out of range")

    def get_cell(self, x, y):
        self._check_bounds(x, y)
        return self.grid[y][x]

    def set_cell(self, x, y, value):
        self._check_bounds(x, y)
        self.grid[y][x] = value

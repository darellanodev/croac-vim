from src.exceptions import BoardIndexError


class Board:
    def __init__(self, layout):
        self.grid = [list(line) for line in layout]

    def get_cell(self, x, y):
        if x < 0 or y < 0:
            raise BoardIndexError("x and y positions must be zero or greater")
        return self.grid[y][x]

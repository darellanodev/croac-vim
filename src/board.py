class Board:
    def __init__(self, layout):
        self.grid = [list(line) for line in layout]

    def get_cell(self, x, y):
        return self.grid[y][x]

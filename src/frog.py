from src.exceptions import InvalidMoveError
from src.board import Board


class Frog:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        if dx != 0 and dy != 0:
            raise InvalidMoveError("Diagonal moves are not allowed")
        self.x += dx
        self.y += dy

    def draw(self, screen, frog_img):
        screen.blit(frog_img, (self.x * Board.CELL_WIDTH, self.y * Board.CELL_HEIGHT))

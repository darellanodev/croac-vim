from src.exceptions import InvalidMoveError
from src.board import Board


class Frog:
    FROG_ANIM_INTERVAL = 300

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.frog_frame = 0

    def move(self, dx, dy):
        if dx != 0 and dy != 0:
            raise InvalidMoveError("Diagonal moves are not allowed")
        self.x += dx
        self.y += dy

    def change_frame(self):
        if self.frog_frame == 0:
            self.frog_frame = 1
        else:
            self.frog_frame = 0

    def update_blink(self):
        self.frame += 1
        if self.frame > self.FROG_ANIM_INTERVAL:
            self.change_frame()
            self.frame = 0

    def draw(self, screen, frog_images):
        screen.blit(
            frog_images[self.frog_frame],
            (self.x * Board.CELL_WIDTH, self.y * Board.CELL_HEIGHT),
        )

from src.exceptions import InvalidMoveError
from src.board import Board
import pygame


class Frog:
    FRAME_MAX_TIME = 300

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame_time = 0
        self.frame = 0

    def move(self, dx, dy):
        if dx != 0 and dy != 0:
            raise InvalidMoveError("Diagonal moves are not allowed")
        self.x += dx
        self.y += dy

    def change_frame(self):
        if self.frame == 0:
            self.frame = 1
        else:
            self.frame = 0

    def update_blink(self):
        self.frame_time += 1
        if self.frame_time > self.FRAME_MAX_TIME:
            self.change_frame()
            self.frame_time = 0

    def draw(self, screen, frog_images):
        screen.blit(
            frog_images[self.frame],
            (self.x * Board.CELL_WIDTH, self.y * Board.CELL_HEIGHT),
        )

    def handle_movement(self, key):
        if key == pygame.K_l:
            self.move(1, 0)
        if key == pygame.K_h:
            self.move(-1, 0)
        if key == pygame.K_j:
            self.move(0, 1)
        if key == pygame.K_k:
            self.move(0, -1)

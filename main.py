import pygame
from src.board import Board
from src.frog import Frog
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()


def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    font = pygame.font.SysFont(None, 48)

    layout = ["The quick brown fox", "jumps over the lazy", "dogs and cat runs"]

    board = Board(layout)
    frog = Frog(0, 0)

    frog_img = pygame.image.load("src/assets/frog_right.png").convert_alpha()
    frog_x, frog_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(Board.BACKGROUND_COLOR)
        board.draw(screen, board, font)
        frog.draw(screen, frog_img)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

import pygame
from src.board import Board
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()


def draw_board(screen, board, font):
    for y in range(len(layout)):
        for x in range(len(layout[y])):
            char = board.get_cell(x, y)
            if char != " ":
                text_surface = font.render(char, True, Board.TEXT_COLOR)
                screen.blit(text_surface, (x * Board.CELL_WIDTH, y * Board.CELL_HEIGHT))


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont(None, 48)

layout = ["The quick brown fox", "jumps over the lazy", "dogs and cat runs"]

board = Board(layout)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Board.BACKGROUND_COLOR)
    draw_board(screen, board, font)
    pygame.display.flip()
pygame.quit()

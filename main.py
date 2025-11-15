import pygame
from src.board import Board

pygame.init()

WIDTH, HEIGHT = 1280, 720
CELL_WIDTH = 40
CELL_HEIGHT = 50
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (12, 34, 63)


def draw_board(screen, board, font):
    for y in range(len(layout)):
        for x in range(len(layout[y])):
            char = board.get_cell(x, y)
            if char != " ":
                text_surface = font.render(char, True, TEXT_COLOR)
                screen.blit(text_surface, (x * CELL_WIDTH, y * CELL_HEIGHT))


screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 48)

layout = ["The quick brown fox", "jumps over the lazy", "dogs and cat runs"]

board = Board(layout)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    draw_board(screen, board, font)
    pygame.display.flip()
pygame.quit()

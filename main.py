import pygame
from src.board import Board

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 48)

layout = ["The quick brown fox", "jumps over the lazy", "dogs and cat runs"]

board = Board(layout)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(((12, 34, 63)))

    for y in range(len(layout)):
        for x in range(len(layout[y])):
            char = board.get_cell(x, y)
            if char != " ":
                text_surface = font.render(char, True, (255, 255, 255))
                screen.blit(text_surface, (x * 40, y * 50))

    pygame.display.flip()
pygame.quit()

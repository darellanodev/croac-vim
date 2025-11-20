import pygame
import asyncio
from src.board import Board
from src.frog import Frog
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()


async def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont(None, 48)
    layout = ["The quick brown fox", "jumps over the lazy", "dogs and cat runs"]
    board = Board(layout)
    frog = Frog(0, 0)
    frog_images = [
        pygame.image.load("src/assets/frog_closed.png").convert_alpha(),
        pygame.image.load("src/assets/frog_open.png").convert_alpha(),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                frog.handle_movement(event.key)

        screen.fill(Board.BACKGROUND_COLOR)
        board.draw(screen, board, font)
        frog.update_blink()
        frog.draw(screen, frog_images)
        pygame.display.flip()

        await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())

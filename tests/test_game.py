import pygame


def test_init_pygame():
    pygame.init()
    assert pygame.get_init() is True

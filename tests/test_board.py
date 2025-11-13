import pytest
from src.board import Board
from src.exceptions import BoardIndexError


def test_board_grid_creation_strings():
    layout = ["The quick brown fox", "jumps over the lazy", "dogs and cat runs"]

    board = Board(layout)

    assert board.get_cell(0, 0) == "T"
    assert board.get_cell(4, 0) == "q"
    assert board.get_cell(4, 1) == "s"


def test_board_get_cell_with_negative_values():
    layout = ["This is a sentence"]

    board = Board(layout)

    with pytest.raises(BoardIndexError):
        board.get_cell(-1, 0)

    with pytest.raises(BoardIndexError):
        board.get_cell(0, -1)


def test_board_get_cell_out_of_range():
    layout = ["This is a sentence"]

    board = Board(layout)

    with pytest.raises(BoardIndexError):
        board.get_cell(0, 1)

    with pytest.raises(BoardIndexError):
        board.get_cell(100, 0)


def test_board_set_cell():
    layout = ["Thxs is a sentence"]

    board = Board(layout)
    board.set_cell(2, 0, "i")

    assert board.get_cell(2, 0) == "i"

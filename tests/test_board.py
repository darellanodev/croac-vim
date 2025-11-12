from src.board import Board


def test_board_grid_creation_strings():
    layout = ["The quick brown fox", "jumps over the lazy", "dogs and cat runs"]

    board = Board(layout)

    assert board.get_cell(0, 0) == "T"
    assert board.get_cell(4, 0) == "q"
    assert board.get_cell(4, 1) == "s"

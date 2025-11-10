import pytest
from src.frog import Frog
from src.exceptions import InvalidMoveError

def test_frog_initial_position():
    frog = Frog(5,7)
    assert frog.x == 5
    assert frog.y == 7

def test_frog_move_position():
    frog = Frog(5,7)
    frog.move(1,0)
    assert frog.x == 6
    assert frog.y == 7

def test_frog_no_diagonal_move():
    frog = Frog(5,7)
    with pytest.raises(InvalidMoveError):
        frog.move(1,1)
from src.frog import Frog

def test_frog_initial_position():
    frog = Frog(5,7)
    assert frog.x == 5
    assert frog.y == 7
from app import add
def test_add():
    assert add(2, 3, 1) == 6
    assert add(-1, 1, 2) == 2
    assert add(0, 0, 0) == 0 
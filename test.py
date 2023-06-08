def test_add_numbers():
    assert add_numbers(1, 2) == 3

def test_add_numbers_with_negative_numbers():
    assert add_numbers(-1, 2) == 1

def test_add_numbers_with_zero():
    assert add_numbers(0, 5) == 5

def test_add_numbers_with_large_numbers():
    assert add_numbers(1000000, 1000000) == 2000000

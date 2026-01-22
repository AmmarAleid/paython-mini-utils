from paython_utils.math_utils import add, is_even


def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    assert add(2.5, 0.5) == 3.0


def test_is_even_true():
    assert is_even(10) is True


def test_is_even_false():
    assert is_even(7) is False

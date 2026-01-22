from paython_utils.string_utils import reverse_string, count_vowels


def test_reverse_string_basic():
    assert reverse_string("Paython") == "nohtyaP"


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_count_vowels_basic():
    assert count_vowels("Paython") == 2


def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0

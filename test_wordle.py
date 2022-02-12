from wordle import calc, calc_one
import pytest


@pytest.mark.parametrize(
    "candidate, real, in_spot, in_word",
    [
        ("stare", "eerie", 1, 1),
        ("eerie", "stare", 1, 1),
        ("eerie", "tease", 2, 0),
        ("round", "eerie", 0, 1),
        ("abcde", "wxyz", 0, 0),
        ("bark", "bare", 3, 0),
        ("robot", "round", 2, 0),
        ("barke", "barek", 3, 2),
        ("abcd", "dcba", 0, 4),
    ],
)
def test_singles(candidate, real, in_spot, in_word):
    found_in_spot, found_in_word = calc_one(candidate, real)
    assert found_in_spot == in_spot
    assert found_in_word == in_word

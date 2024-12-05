from collections import Counter

import pytest


def most_frequent_char(word):
    c_counts = Counter(word)
    most_frequent = None
    for k, v in c_counts.items():
        if most_frequent is None or v > c_counts[most_frequent]:
            most_frequent = k
    return most_frequent


@pytest.mark.parametrize(
    "word,expected",
    [
        ("tree", "e"),
        ("oblivian", "i"),
        ("sunshine", "s"),
        ("cheese", "e"),
        ("boob", "b"),  # The letter that appears first wins if more than one
        ("potato", "o"),
    ],
)
def test_most_frequent_char(word, expected):
    assert most_frequent_char(word) == expected

import pytest


def intersection_slow(a, b):
    intersection = []
    for i in a:
        if i in b:
            intersection.append(i)
    return intersection


def intersection_set(a, b):
    return list(set(a) & set(b))



@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([4, 2, 1, 6], [3, 6, 9, 2, 10], [2, 6]),
        ([2, 4, 6], [4, 2], [2, 4]),
        ([4, 2, 1], [1, 2, 4, 6], [1, 2, 4]),
    ],
)
def test_intersection(a, b, expected):
    assert intersection_set(a, b) == expected

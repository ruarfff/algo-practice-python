import pytest


# O(n) - space O(n)
def pair_product(nums, product):
    lookup = {}
    for i, n in enumerate(nums):
        compliment = product / n
        if compliment in lookup:
            return (lookup[compliment], i)
        lookup[n] = i


@pytest.mark.parametrize(
    "nums,product,expected",
    [
        ([3, 2, 5, 4, 1], 8, (1, 3)),
        ([3, 2, 5, 4, 1], 10, (1, 2)),
        ([4, 7, 9, 2, 5, 1], 5, (4, 5)),
    ],
)
def test_pair_sum(nums, product, expected):
    assert pair_product(nums, product) == expected

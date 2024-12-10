import pytest


def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


countdown(3)


def recursive_sum(nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(nums[1:])

@pytest.mark.parametrize(
    "nums,expected",
    [
        ([5, 2, 9, 10], 26),
        ([1, -1, 1, -1, 1, -1, 1], 1),
        ([], 0),
        ([1000, 0, 0, 0, 0, 0, 1], 1001),
    ],
)
def test_recursive_sum(nums, expected):
    assert recursive_sum(nums) == expected

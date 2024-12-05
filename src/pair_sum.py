import pytest

# O(n2) - space O(1)
# def pair_sum(nums: int, sum: int) -> tuple[int, int]:
#     for i, n1 in enumerate(nums):
#         for j, n2 in enumerate(nums):
#             if i != j and n1 + n2 == sum:
#                 return (i, j)
#     return ()


# O(n) - space O(n)
def pair_sum(nums: int, sum: int) -> tuple[int, int] | None:
    lookup = {nums[0]: 0}
    for i in range(1, len(nums)):
        compliment = sum - nums[i]
        if compliment in lookup:
            return (lookup[compliment], i)
        lookup[nums[i]] = i
    return None


@pytest.mark.parametrize(
    "nums,sum,expected",
    [
        ([3, 2, 5, 4, 1], 8, (0, 2)),
        ([4, 7, 9, 2, 5, 1], 5, (0, 5)),
        ([4, 7, 9, 2, 5, 1], 3, (3, 5)),
    ],
)
def test_pair_sum(nums, sum, expected):
    assert pair_sum(nums, sum) == expected

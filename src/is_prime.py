from math import sqrt
def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

assert not is_prime(1)
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert is_prime(5)
assert is_prime(67)


def better_is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


assert not better_is_prime(1)
assert better_is_prime(2)
assert better_is_prime(3)
assert not better_is_prime(4)
assert better_is_prime(5)
assert not better_is_prime(64)
assert better_is_prime(67)

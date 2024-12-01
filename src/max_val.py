def max_val(input: list[int]) -> int:
    max_val = input[0]
    for i in input:
        if i > max_val:
            max_val = i
    return max_val


print(max_val([1, 2, 3, 4, 5])) # 5
print(max_val([17, 5, 4, 3, 2, 1])) # 17
print(max_val([1, 2, 5, 21, 4, 3])) # 21
print(max_val([1, 2, 5, 21, 55, 4, 3])) # 55

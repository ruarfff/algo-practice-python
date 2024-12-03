def count_chars(s):
    chr_counts = {}
    for c in s:
        if c not in chr_counts:
            chr_counts[c] = 0
        chr_counts[c] += 1
    return chr_counts

def is_anagram(s1, s2):
    s1_counts = count_chars(s1)
    s2_counts = count_chars(s2)
    return s1_counts == s2_counts


assert is_anagram('abc', 'bca')
assert not is_anagram('abc', 'bcaa')
assert is_anagram('abca', 'bcaa')
assert is_anagram('bored', 'robed')
assert not is_anagram('boreds', 'robed')

print('anagram - All test passed')

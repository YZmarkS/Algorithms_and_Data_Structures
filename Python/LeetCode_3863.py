def minOperations(s: str) -> int:
    n = len(s)
    last_char = 'A'
    is_non_descending = True
    counts = dict()
    for i in range(n):
        char = s[i]
        counts[char] = counts.get(char, 0) + 1
        if last_char > char:
            is_non_descending = False
        last_char = char

    if is_non_descending:
        return 0
    if n == 2:
        return -1

    min_char = min(counts.keys())
    max_char = max(counts.keys())

    if s[0] == min_char or s[n - 1] == max_char:
        return 1
    if s[n - 1] != min_char:
        return 2
    if s[0] != max_char:
        return 2
    if 2 <= counts[min_char] or 2 <= counts[max_char]:
        return 2
    return 3

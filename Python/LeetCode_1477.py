import bisect

def minSumOfLengths(arr: List[int], target: int) -> int:
    n = len(arr)
    psa = [ 0 for _ in range(n + 1) ]
    for i in range(0, n):
        psa[i + 1] = psa[i] + arr[i]

    intervals = []
    for i in range(0, n):
        curr_acc = psa[i]
        want_acc = curr_acc + target
        index = bisect.bisect_left(psa, want_acc, i + 1, n + 1)
        if index < n + 1 and psa[index] == want_acc:
            intervals.append((i, index)) # summ(arr[i, index]) == target
        else:
            intervals.append(None)

    shortests = [ -1 for i in range(n + 1) ]
    for i in range(n - 1, -1, -1):
        if intervals[i] is None:
            shortests[i] = shortests[i + 1]
        else:
            (j, k) = intervals[i]
            length = k - j
            if shortests[i + 1] == -1:
                shortests[i] = length
            else:
                shortests[i] = min(shortests[i + 1], length)

    found = False
    result = n + 1
    for i in range(n):
        if intervals[i] is None:
            continue
        (j, k) = intervals[i]
        if shortests[k] == -1:
            continue
        new_total = k - j + shortests[k]
        found = True
        result = min(result, new_total)

    if found:
        return result
    return -1

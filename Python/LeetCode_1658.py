def minOperations(nums: List[int], x: int) -> int:
    n = len(nums)
    total = sum(nums)
    target = total - x
    psa = [ 0 for _ in range(n + 1) ]
    for i in range(n):
        psa[i + 1] = psa[i] + nums[i]

    i, j = 0, 0
    best = n + 1
    while j <= n:
        diff = psa[j] - psa[i]
        if diff == target:
            best = min(best, n - (j - i))
            i += 1
        elif diff < target or i == j:
            j += 1
        elif target < diff:
            i += 1
        print(i, j, best)
    return -1 if best == n + 1 else best

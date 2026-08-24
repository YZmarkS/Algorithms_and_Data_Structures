def uniquePaths(m : int, n : int) -> int:
    prev = [ 1 for _ in range(n) ]
    for _ in range(m-1):
        curr = [ 0 for _ in range(n) ]
        curr[0] = 1
        for j in range(1, n):
            curr[j] = curr[j - 1] + prev[j]
        prev = curr
    return prev[n-1]

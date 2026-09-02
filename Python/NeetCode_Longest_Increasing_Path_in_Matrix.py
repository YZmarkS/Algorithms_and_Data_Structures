def longestIncreasingPath(matrix: List[List[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    def in_bound(r: int, c: int) -> bool:
        return 0 <= r < n and 0 <= c < n

    dp = [ [ None for _ in range(m) ] for _ in range(n) ]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def calc(r: int, c: int) -> int:
        if dp[r][c] is not None:
            return dp[r][c]
        best = 1
        for (dr, dc) in directions:
            pr, pc = r + dr, c + dc
            if in_bound(pr, pc) and matrix[r][c] > matrix[pr][pc]:
                best = max(best, calc(pr, pc) + 1)
        dp[r][c] = best
        return best

    ans = 0
    for r in range(n):
        for c in range(m):
           ans = max(ans, calc(r, c))
    return ans

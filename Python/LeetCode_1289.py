def minFallingPathSum(grid: list[list[int]]) -> int:
    n = len(grid)

    if n == 1:
        return grid[0][0]


    dp = [ [ 100 * 200 + 1 for _ in range(n) ] for _ in range(n) ]

    for i in range(n):
        dp[0][i] = grid[0][i]
    two_best = []
    ascending = list(sorted(zip(grid[0], range(n))))
    two_best.extend(ascending[0:2])

    for i in range(1, n):
        print(two_best)
        for j in range(n):
            dp[i][j] = grid[i][j] + (two_best[0][0] if two_best[0][1] != j else two_best[1][0])
        two_best = []
        ascending = list(sorted(zip(dp[i], range(n))))
        two_best.extend(ascending[0:2])

    return two_best[0][0]

def minDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    dp = [ [ -1 for _ in range(m + 1) ] for _ in range(n + 1) ]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c1 = word1[i - 1]
            c2 = word2[j - 1]
            dp[i][j] = min(dp[i - 1][j - 1] + (0 if c1 == c2 else 1), \
                           dp[i][j - 1] + 1, \
                           dp[i - 1][j] + 1)

    return dp[n][m]

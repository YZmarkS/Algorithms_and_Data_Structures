def numDecodings(s: str) -> int:
    n = len(s)
    if n == 1:
        return 1 if s[0] != '0' else 0
    dp = [ 0 for _ in range(n) ]
    dp[0] = 1 if s[0] != '0' else 0
    dp[1] += dp[0] if s[1] != '0' else 0
    dp[1] += 1 if 10 <= int(s[0:2]) <= 26 else 0

    for i in range(2, n):
        last_char = s[i]
        last_two_char = s[i - 1: i + 1]

        if last_char != '0':
            dp[i] += dp[i - 1]
        if 10 <= int(last_two_char) <= 26:
            dp[i] += dp[i - 2]

    print(dp)
    return dp[n - 1]

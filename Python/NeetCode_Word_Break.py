def wordBreak(s: str, wordDict: List[str]) -> bool:
    length = len(s)
    dp = [False for _ in range(length + 1)]
    dp[0] = True
    for i in range(1, length + 1, 1):
        for tgt in wordDict:
            sub_len = len(tgt)
            start = i - sub_len
            if 0 <= start:
                dp[i] = dp[i] or (dp[start] and s[start:i] == tgt)

    return dp[length]

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)

    if s1_len + s2_len != s3_len:
        return False

    # Can interleave s1[i:s1_len], s2[j:s2_len] into a suffix of s3
    dp = [ [ False for _ in range(s2_len + 1) ] for _ in range(s1_len + 1) ]

    dp[s1_len][s2_len] = True
    # for i in range(s1_len - 1, -1, -1):
    #     curr_len = s1_len - i
    #     dp[i][s2_len] = dp[i + 1][s2_len] and s1[i] == s3[s3_len - curr_len]
    for s2_sub_len in range(1, s2_len + 1):
        j = s2_len - s2_sub_len
        dp[s1_len][j] = dp[s1_len][j + 1] and s2[j] == s3[s3_len - s2_sub_len]

    for s1_sub_len in range(1, s1_len + 1):
        i = s1_len - s1_sub_len
        dp[i][s2_len] = dp[i + 1][s2_len] and s1[i] == s3[s3_len - s1_sub_len]
        for s2_sub_len in range(1, s2_len + 1):
            j = s2_len - s2_sub_len
            dp[i][j] = \
                (dp[i + 1][j] and s1[i] == s3[s3_len - (s1_sub_len + s2_sub_len)]) or \
                (dp[i][j + 1] and s2[j] == s3[s3_len - (s1_sub_len + s2_sub_len)])

    return dp[0][0]

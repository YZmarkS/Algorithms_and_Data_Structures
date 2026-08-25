def maxProfit(prices : List[int]) -> int:
    length = len(prices)
    dp0 = [ 0 for _ in range(length) ] # best cost with 0 coin on day i
    dp1 = [ 0 for _ in range(length) ] # best cost with 1 coin on day i

    dp0[0] = 0
    dp1[0] = -prices[0]

    for i in range(1, length):


        dp0_val = max(dp0[0:i])
        for j in range(0, i):
            dp0_val = max(dp0_val, dp1[j] + prices[i])
        dp1_val = max(dp1[0:i], -price[i])
        for j in range(0, i - 1):
            dp1_val = max(dp1_val, dp0[j] - prices[i])
        dp0[i] = dp0_val
        dp1[i] = dp1_val

        print(i, "=========")
        print(dp0)
        print(dp1)

    return max(dp0[length - 1], dp1[length - 1])

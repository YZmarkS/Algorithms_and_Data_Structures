def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    miss_0_dp = [ 0 for _ in range(n) ]
    take_0_dp = [ 0 for _ in range(n) ]
    take_0_dp[0] = nums[0]
    take_0_dp[1] = nums[0]
    miss_0_dp[1] = nums[1]
    for i in range(2, n - 1):
        miss_0_dp[i] = nums[i] + max(miss_0_dp[:i - 1])
        take_0_dp[i] = nums[i] + max(take_0_dp[:i - 1])

    miss_0_dp[n-1] = nums[n-1] + max(miss_0_dp[:n - 2])

    return max(max(miss_0_dp), max(take_0_dp[:-1]))

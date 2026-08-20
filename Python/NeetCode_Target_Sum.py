def findTargetSumWays(nums: List[int], target: int) -> int:
    bound = sum(nums) * 2 + 1
    zero = sum(nums)
    if target < -zero or zero < target:
        return 0
    old_dp = [ 0 for _ in range(bound) ]
    old_dp[zero] = 1

    for num in nums:
        new_dp = [ 0 for _ in range(bound) ]
        for i in range(bound):
            subtract = i - num
            if 0 <= subtract and subtract <= bound - 1:
                new_dp[subtract] += old_dp[i]
            addition = i + num
            if 0 <= addition and addition <= bound - 1:
                new_dp[addition] += old_dp[i]
        old_dp = new_dp
        print(old_dp)
    return old_dp[zero + target]

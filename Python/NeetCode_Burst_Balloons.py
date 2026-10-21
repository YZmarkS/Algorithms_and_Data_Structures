def maxCoins(nums: List[int]) -> int:
    n = len(nums)
    nums.insert(0, 1)
    nums.append(1)

    dp = dict()

    def solve(l, r):
        if (l, r) in dp:
            return dp[(l, r)]
        if l == r:
            best = nums[l - 1] * nums[l] * nums[r + 1]
            dp[(l, r)] = nums[l - 1] * nums[l] * nums[r + 1]
            return best
        else:
            pop_left_last = \
                nums[l - 1] * nums[l] * nums[r + 1] + solve(l + 1, r)
            pop_mid_last = 0
            for i in range(l + 1, r):
                pop_mid_last = max(pop_mid_last, \
                                   nums[l - 1] * nums[i] * nums[r + 1] \
                                   + solve(l, i - 1) + solve(i + 1, r))
            pop_right_last = \
                nums[l - 1] * nums[r] * nums[r + 1] + solve(l, r - 1)

            best = max(pop_left_last, \
                       pop_mid_last, \
                       pop_right_last)
            dp[(l, r)] = best
            return best

    return solve(1, n)

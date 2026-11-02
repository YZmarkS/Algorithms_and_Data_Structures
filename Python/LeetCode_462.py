def minMoves2(nums: list[int]) -> int:
    n = len(nums)
    nums = sorted(nums)

    target = nums[n // 2]
    return sum(map(lambda num : abs(num - target), nums))

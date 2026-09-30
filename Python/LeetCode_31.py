l1 = [1, 2, 3]
l2 = [3, 2, 1]
l3 = [1, 1, 5]

def nextPermutation(nums: list[int]) -> None:
    n = len(nums)
    peak = n - 1
    while peak > 0:
        if nums[peak - 1] < nums[peak]:
            break
        peak -= 1

    before_peak = peak - 1

    if 0 <= before_peak:
        tail = nums[peak:]
        tail_rev = list(reversed(tail))
        i = 0
        while tail_rev[i] <= nums[before_peak]:
            i += 1
        nums[before_peak], tail_rev[i] = tail_rev[i], nums[before_peak]
        for i in range(len(tail_rev)):
            nums[peak + i] = tail_rev[i]
    else:
        nums.reverse()

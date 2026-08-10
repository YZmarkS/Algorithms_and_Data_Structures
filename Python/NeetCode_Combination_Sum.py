def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    length = len(nums)
    ans = []
    def aux(total, index, acc):
        if target < total or length <= index:
            return
        if total == target:
            ans.append(acc.copy())
            return
        acc.append(nums[index])
        aux(total + nums[index], index, acc)
        acc.pop()
        aux(total, index + 1, acc)

    aux(0, 0, [])
    return ans

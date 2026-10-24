def minOperations(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    elif n == 2:
        return 0 if nums[0] == 0 else 1

    index_of_zero = -1
    for i in range(n):
        if nums[i] == 0:
            index_of_zero = i
            break
    opposite_index = n - 1 - index_of_zero

    # Check is ascending:
    is_ascending = True
    is_descending = True
    for i in range(n):
        if nums[ (index_of_zero + i) % n ] != i:
            is_ascending = False
        if nums[ (index_of_zero - i) % n ] != i:
            is_descending = False

    if is_ascending:
        return min(index_of_zero, 1 + opposite_index + 1 + 1)
    if is_descending:
        return min(index_of_zero + 1 + 1, 1 + opposite_index)

    return -1

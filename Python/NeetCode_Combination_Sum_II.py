def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    counter = dict()
    for candidate in candidates:
        counter[candidate] = 1 + (counter[candidate] if candidate in counter else 0)
    candidates_with_count = list(counter.items())

    result = []

    def backtrack(remains: List[tuple[int, int]], acc: List[int]):
        curr_sum = sum(acc)
        if curr_sum == target:
            result.append(acc.copy())
            return
        if curr_sum > target \
           or not remains:
            return

        (elem, count) = remains[0]
        tail = remains[1:]
        backtrack(tail, acc)

        for _ in range(count):
            acc.append(elem)
            backtrack(tail, acc)
        for _ in range(count):
            acc.pop()
        return

    backtrack(candidates_with_count, [])
    return result

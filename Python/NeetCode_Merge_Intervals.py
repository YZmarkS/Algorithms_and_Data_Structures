from collections import deque

def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)

    if n == 0:
        return []

    sorted_intervals = list(map(lambda i : [i[1], i[0]], \
                                sorted(list(map(lambda i : [i[1], i[0]], \
                                                intervals)))))

    print(sorted_intervals)

    def overlap(i1, i2):
        return i2[0] <= i1[1]

    def merge(i1, i2):
        return [min(i1[0], i2[0]), max(i1[1], i2[1])]

    result = []
    q = deque(sorted_intervals)

    while q:
        print("===")
        curr = q.popleft()
        print(curr)

        while result and overlap(result[-1], curr):
            last = result.pop()
            curr = merge(last, curr)

        result.append(curr)

        print(result)

    return result

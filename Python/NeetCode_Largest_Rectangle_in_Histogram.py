def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    first_left = [ -1 for _ in range(n) ]
    first_right = [ n for _ in range(n) ]

    stack = []
    for i in range(0, n, 1):
        while stack and heights[i] <= heights[stack[-1]]:
            stack.pop()
        if stack:
            first_left[i] = stack[-1]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and heights[i] <= heights[stack[-1]]:
            stack.pop()
        if stack:
            first_right[i] = stack[-1]
        stack.append(i)

    best = 0
    for i in range(n):
        curr_max = (first_right[i] - first_left[i] - 1) * heights[i]
        best = max(best, curr_max)

    return best


"""
Perspective is important.

A natural (and naive) way to search for the best rectangle is:
> For each index i, what is the biggest rectangle starting at index i

However, the correct perspective here should be:
> For each index i, what is the biggest rectangle with height of heights[i] and
> includes the index i?
"""

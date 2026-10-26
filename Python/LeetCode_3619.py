def countIslands(grid: List[List[int]], k: int) -> int:
    r = len(grid)
    c = len(grid[0])
    directions = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
    visited = set()

    def in_bound(row, col):
        return 0 <= row < r and 0 <= col < c

    def flood(row, col):
        total = grid[row][col]
        for (dr, dc) in directions:
            row_ = row + dr
            col_ = col + dc
            if in_bound(row_, col_) \
               and (row_, col_) not in visited \
               and 0 < grid[row_][col_]:
                visited.add( (row_, col_) )
                total += flood(row_, col_)
        return total

    count = 0
    for row in range(r):
        for col in range(c):
            if (row, col) not in visited and 0 < grid[row][col]:
                visited.add( (row, col) )
                subtotal = flood(row, col)
                print(row, col, subtotal)
                if subtotal % k == 0:
                    count += 1

    return count

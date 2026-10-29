def swimInWater(grid: List[List[int]]) -> int:
    r = len(grid)
    c = len(grid[0])
    directions = [(0, 1), (1, 0)]
    dsu = [ [ (row, col) for col in range(c) ] for row in range(r) ]
    elevations = set()
    for row in grid:
        for elevation in row:
            elevations.add(elevation)
    elevations = sorted(list(elevations))

    def find(row, col):
        while dsu[row][col] != (row, col):
            (next_row, next_col) = dsu[row][col]
            (next_next_row, next_next_col) = dsu[next_row][next_col]
            dsu[row][col] = (next_next_row, next_next_col)
            row, col = next_row, next_col
        return (row, col)

    def union(row1, col1, row2, col2):
        if (row1, col1) <= (row2, col2):
            dsu[row2][col2] = (row1, col1)
        else:
            dsu[row1][col1] = (row2, col2)

    def in_bound(row, col):
        return 0 <= row < r and 0 <= col < c

    for elevation in elevations:
        for row in range(r):
            for col in range(c):
                if grid[row][col] <= elevation:
                    for dr, dc in directions:
                        row_, col_ = row + dr, col + dc
                        if in_bound(row_, col_) and grid[row_][col_] <= elevation:
                            (row1, col1) = find(row, col)
                            (row2, col2) = find(row_, col_)
                            union(row1, col1, row2, col2)
        (row1, col1) = find(0, 0)
        (row2, col2) = find(r - 1, c - 1)
        if (row1, col1) == (row2, col2):
            return elevation

    return -1

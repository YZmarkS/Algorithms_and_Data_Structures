def solveNQueens(n : int) -> List[List[str]]:
    solutions = []
    board = [ [ False for _ in range(n) ] for _ in range(n) ]
    col_usage = set()
    diag_usage_1 = set()
    diag_usage_2 = set()

    def attacks(r: int, c: int) -> bool:
        return c in col_usage or r - c in diag_usage_1 or r + c in diag_usage_2

    def board_to_solution():
        rows = []
        for r in range(n):
            row = ""
            for c in range(n):
                row += "Q" if board[r][c] else "."
            rows.append(row)
        return rows

    def place_queen(r: int):
        if r == n:
            solutions.append(board_to_solution())
            return
        for c in range(n):
            if not attacks(r, c):

                board[r][c] = True
                col_usage.add(c)
                diag_usage_1.add(r - c)
                diag_usage_2.add(r + c)

                place_queen(r + 1)
                board[r][c] = False
                col_usage.remove(c)
                diag_usage_1.remove(r - c)
                diag_usage_2.remove(r + c)

    place_queen(0)
    return solutions

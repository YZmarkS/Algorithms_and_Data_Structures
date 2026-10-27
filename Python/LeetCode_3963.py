def createGrid(m: int, n: int) -> list[str]:
    result = []
    result.append("." * n)
    for _ in range(m - 1):
        result.append("#" * (n - 1) + ".")
    return result

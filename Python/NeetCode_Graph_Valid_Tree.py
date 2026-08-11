from collections import deque

def validTree(n : int, edges: List[List[int]]) -> bool:
    g = [ [] for _ in range(n) ]
    for [src, tgt] in edges:
        g[src].append(tgt)
        g[tgt].append(src)

    visited = set()
    q = deque([])
    q.append(0)
    while q:
        top = q.popleft()
        if top in visited:
            continue
        visited.add(top)
        for tgt in g[top]:
            q.append(tgt)
    return len(edges) == n - 1 if len(visited) == n else False

from collections import deque

def countComponents(n: int, edges: List[List[int]]) -> int:
    count = 0
    visited = set()
    g = [ [] for _ in range(n) ]
    for [u, v] in edges:
        g[u].append(v)
        g[v].append(u)

    for i in range(n):
        if i in visited:
            continue

        count += 1
        q = deque([i])
        visited.add(i)
        while q:
            u = q.popleft()
            for v in g[u]:
                if v in visited:
                    continue
                q.append(v)
                visited.add(v)

    return count

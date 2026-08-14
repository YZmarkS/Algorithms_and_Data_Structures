from collections import deque

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    disjoint_union = [ i for i in range(n + 1) ]

    def get_rep(i):
        curr = i
        while disjoint_union[curr] != curr:
            curr = disjoint_union[curr]
        disjoint_union[i] = curr
        return curr

    for [src, tgt] in edges:
        src_rep, tgt_rep = get_rep(src), get_rep(tgt)
        if src_rep == tgt_rep:
            return [src, tgt]
        disjoint_union[tgt_rep] = src_rep
    return []

def findRedundantConnection_(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    g = [ [] for _ in range(n + 1) ]
    for [src, tgt] in edges:
        g[src].append(tgt)
        g[tgt].append(src)

    def still_connected(src, tgt):
        q = deque([1])
        visited = set([1])
        while q:
            curr = q.popleft()
            for next in g[curr]:
                if (curr, next) != (src, tgt) and (next, curr) != (src, tgt) and \
                   next not in visited:
                    q.append(next)
                    visited.add(next)
        return len(visited) == n

    for i in range(n-1, -1, -1):
        [src, tgt] = edges[i]
        if still_connected(src, tgt):
            return edges[i]
    return []

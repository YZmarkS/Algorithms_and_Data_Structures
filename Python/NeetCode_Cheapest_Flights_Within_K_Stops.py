from collections import deque
import heapq

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    distances = [ 100 * 1000 + 1 for _ in range(n) ]
    distances[src] = 0
    g = [ [ None for _ in range(n) ] for _ in range(n) ]
    for [s, tgt, price] in flights:
        g[s][tgt] = price
    visited = set([src])
    for _ in range(k + 1):
        print(visited, distances)
        new_distances = distances.copy()
        new_visited = set()
        for top in visited:
            new_visited.add(top)
            for tgt in range(n):
                if g[top][tgt] is not None:
                    new_distances[tgt] = min(distances[top] + g[top][tgt], new_distances[tgt])
                    new_visited.add(tgt)
        distances = new_distances
        visited = new_visited
        print(visited, distances)

    return -1 if distances[dst] == 100 * 1000 + 1 else distances[dst]

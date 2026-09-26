from collections import defaultdict

def findItinerary(tickets: List[List[str]]) -> List[str]:
    n = len(tickets);
    g = dict()
    degree = dict()
    airports = set()
    for [src, tgt] in tickets:
        airports.add(src)
        airports.add(tgt)
        if src in g:
            g[src].append(tgt)
        else:
            g[src] = [tgt]
        degree[src] = degree.get(src, 0) + 1
        degree[tgt] = degree.get(tgt, 0) - 1

    for airport in g.keys():
        g[airport].sort()

    odd_node = None
    for airport in airports:
        if airport != "JFK" and degree[airport] == -1:
            odd_node = airport

    print(odd_node)

    if odd_node is not None:
        if odd_node in g:
            g[odd_node].insert(0, "JFK")
        else:
            g[odd_node] = ["JFK"]

    def insertAtLastOccurence(acc, elem, to_insert):
        if acc == []:
            acc.extend(to_insert)
        else:
            index = -1
            for i in range(len(acc) - 1, -1, -1):
                if acc[i] == elem:
                    index = i
                    break
            for i in range(len(to_insert) - 1 - 1, -1, -1):
                acc.insert(index, to_insert[i])

    def findLastOccurenceInSet(acc, s):
        for i in range(len(acc) - 1, -1, -1):
            if acc[i] in s:
                return acc[i]

    curr = odd_node if odd_node is not None else "JFK"
    acc_path = []
    curr_path = [curr]
    for _ in range(n + (1 if odd_node is not None else 0)):
        print(g)
        print(acc_path, curr_path, curr)
        if curr not in g.keys():
            insertAtLastOccurence(acc_path, curr_path[0], curr_path)
            curr = findLastOccurenceInSet(acc_path, g.keys())
            curr_path = [curr]

        next = g[curr][0]
        curr_path.append(next)
        g[curr].pop(0)
        if g[curr] == []:
            g.pop(curr)
        curr = next

    insertAtLastOccurence(acc_path, curr_path[0], curr_path)

    if odd_node is not None:
        acc_path.pop(0)

    return acc_path

"""
Borrowed Hierholzer's Algorithm from the internet:
https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer's_algorithm
https://dxing.blog/Algorithms/Hierholzer's-Algorithm

The graph, as given, has two cases:
1. Every node n has in(n) == out(n)
2. out(JFK) == in(JFK) + 1 and out(o) == in(o) - 1, for some node o

Case 1: Start from JFK
Case 2: Start from o, immediately go to JFK

Before walking through the graph, there are three variables we track:
1. acc, this will be the actual answer we return, so starts empty
2. curr, current node
3. curr_path, this is the current path we are on, and each time it
                gets reset to [curr]

Start walking through the graph. At each step, choose the edge that leads
to the node with the lowest lexical ordering. After taking the edge, remove
it from the graph.

If at any point, there are no edges to take, it can be proven that we are
guaranteed to have returned to curr_path[0]. Now insert curr_path into acc
at the lastest possible point. For example:

acc = [2, 1, 2, 3]
curr_path = [2, 4, 5, 2]
Then insert curr_path at index 2 of acc, resulting in acc = [2, 1, 2, 4, 5, 2, 3]

Reset curr to be the last element in acc such that the node still has an
outgoing edge.

Repeat for len(tickets) steps, which will use up all possible edges.
After the loop, need to insert curr_path into acc one more time.
"""

def numberOfEdgesAdded(n : int, edges: List[List[int]]) -> int:
    dsu = [ i for i in range(n) ]
    dist_to_parent = [ 0 for i in range(n) ]
    colour = [ True for i in range(n) ]
    same_colour_as_parent = [ True for i in range(n) ]

    """
    By the end of this function, every node along the path points
    directly to representative. dist_to_parent and same_colour_as_parent
    are updated accordingly.
    """
    def find_rep_dist_sameness(i):
        if dsu[i] == i:
            return (i, 0, True)
        next = dsu[i]
        # IH, dsu[next] points to representative
        #     dist_to_rep = distance from 'next' to rep
        #     is_same_as_rep = is 'next's colour same as rep
        (rep, dist_to_rep, is_same_as_rep) = find_rep_dist_sameness(next)
        dsu[i] = rep
        dist_to_parent[i] += dist_to_rep
        same_colour_as_parent[i] = \
            (same_colour_as_parent[i] and is_same_as_rep) \
            or \
            (not same_colour_as_parent[i] and not is_same_as_rep)
        return (rep, dist_to_parent[i], same_colour_as_parent[i])

    total = 0
    for [u, v, w] in edges:

        u_rep, u_dist_to_u_rep, u_same_as_rep = find_rep_dist_sameness(u)
        v_rep, v_dist_to_v_rep, v_same_as_rep = find_rep_dist_sameness(v)

        if u_rep != v_rep:
            lower_rep, higher_rep = min(u_rep, v_rep), max(u_rep, v_rep)
            distance = u_dist_to_u_rep + v_dist_to_v_rep + w
            dsu[higher_rep] = lower_rep
            dist_to_parent[higher_rep] = distance
            same_colour_as_parent[higher_rep] = distance % 2 == 0

            total += 1
        else: # u_rep == v_rep
            u_colour = colour[u_rep] if u_same_as_rep else not colour[u_rep]
            v_colour = colour[v_rep] if v_same_as_rep else not colour[v_rep]
            if u_colour == v_colour and w % 2 == 0 \
               or u_colour != v_colour and w % 2 == 1:
                total += 1

    return total

"""
Suppose every connected component is free of odd cycle,
then it is always possible to connect two components.

So we use disjoint union set as the main solution.

To determine the colour of a node, we calculate what is it's colour
relative to the representative. To avoid computing for nodes we may
not need after every union, we instead track the colour relative to
parent (in the union set sense). On query, the path from the queried
node to the representative are collapsed.

There are two cases for each edge:
1. If the representative of two nodes to be connected are different,
we can always union them. Suppose rep_u < rep_v, and we choose the
representative to always be the lower number, then the colour of rep_v
needs depends on the distance from rep_u to rep_v. The distance is
equal to d(rep_u, u) + d(rep_v, v) + w. So remember to track distance.
2. If the representative of two nodes are the same, simply check if
the colour of the two nodes are compatible with the weight.
Same colour is compatible with even w, diff colour is compatible with
odd w.
"""

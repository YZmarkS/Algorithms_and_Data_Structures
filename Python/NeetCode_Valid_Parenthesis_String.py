def checkValidString(s: str) -> bool:
    lefts = []
    stars = []
    index = 0
    for c in s:
        if c == "(":
            lefts.append(index)
        elif c == "*":
            stars.append(index)
        elif c == ")":
            if not lefts and not stars:
                return False
            if lefts:
                lefts.pop()
            else:
                stars.pop()
        index += 1

    while lefts and stars:
        right_most_left = lefts.pop()
        right_most_star = stars.pop()
        if right_most_left > right_most_star:
            return False

    return not lefts

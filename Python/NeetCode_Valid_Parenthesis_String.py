def checkValidString(s: str) -> bool:
    length = len(s)
    diffs = [0] * length
    diff = 0
    for i in range(length):
        c = s[i]
        if c == '(':
            diff += 1
        elif c == ')':
            diff -= 1
        diffs[i] = diff

def sumGame(num: str) -> bool:
    left_total, right_total = 0, 0
    left_spots, right_spots = 0, 0
    length = len(num)
    for i in range(0, length // 2):
        if num[i] == '?':
            left_spots += 1
        else:
            left_total += int(num[i])
    for j in range(length // 2, length):
        if num[j] == '?':
            right_spots += 1
        else:
            right_total += int(num[j])

    if (left_spots + right_spots) % 2 == 1:
        return True

    higher_total, lower_total = 0, 0
    higher_spots, lower_spots = 0, 0
    if left_total > right_total:
        higher_total, lower_total = left_total, right_total
        higher_spots, lower_spots = left_spots, right_spots
    else:
        higher_total, lower_total = right_total, left_total
        higher_spots, lower_spots = right_spots, left_spots

    return (higher_total - lower_total) != (lower_spots - higher_spots) // 2 * 9

"""
Notice if there are odd number of '?', Alice always gets last pick
and can pick whatever that makes both sides unequal.

WLOG, Assume the left side always have greater total

Notice if all the '?' are on one side, then Bob can win if and only if
1. All the '?' are on the right side
2. left sum - right sum == 9 * ('?' count / 2)
This is because Bob can always complement Alice's choice to add 9 to
right side every two picks.
If the equality doesn't hold, Alice can either choose all 9 or all 0
so Bob cannot possible reach the difference using his own picks alone.

Now consider the generic case, we claim:
Bob wins if (left sum - right sum) == 9 * (right '?' count - left '?' count) / 2
Alice wins otherwise

Intuitively, if the equation doesn't hold, Alice can ensure the
equation never holds, and so Bob never reaches his winning condition.

if (left sum - right sum) < 9 * (right '?' count - left '?' count) / 2
Alice can pick 9 on the right, making the difference even smaller
and Bob cannot possibly recover.

if (left sum - right sum) > 9 * (right '?' count - left '?' count) / 2
Alice can pick 9 on the left, making the difference even greater
and Bob cannot possibly recover.

By the time one side is all picked, we will have an inequality that
does not satisfy Bob's winning condition, hence Alice wins.

if the equality held at the beginning, Bob can always complement
Alice's pick by picking an equal number on the opposite side, and keep
the equality hold.
"""

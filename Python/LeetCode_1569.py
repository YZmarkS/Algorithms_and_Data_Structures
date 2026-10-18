import math

def numOfWays(nums: list[int]) -> int:
    MOD = int(1e9 + 7)
    n = len(nums)
    zipped = list(zip(nums, range(n)))

    LEFT_SIZE, RIGHT_SIZE, LEFT_INDEX, RIGHT_INDEX = 0, 1, 2, 3
    tree = [ [0, 0, -1, -1] for _ in range(n) ]

    def build_tree(inserts):
        (num, index) = inserts[0]
        tail = inserts[1:]
        left_inserts = list(filter(lambda pair: pair[0] < num, tail))
        right_inserts = list(filter(lambda pair: num < pair[0], tail))

        if left_inserts:
            left_index = left_inserts[0][1]
            tree[index][LEFT_SIZE] = len(left_inserts)
            tree[index][LEFT_INDEX] = left_index
            build_tree(left_inserts)
        if right_inserts:
            right_index = right_inserts[0][1]
            tree[index][RIGHT_SIZE] = len(right_inserts)
            tree[index][RIGHT_INDEX] = right_index
            build_tree(right_inserts)


    build_tree(zipped)

    def calc_ways(index: int):
        [left_size, right_size, left_index, right_index] = tree[index]


        if left_size == 0 and right_size == 0:
            return 1

        if left_size == 0 and 0 < right_size:
            return calc_ways(right_index)
        elif 0 < left_size and right_size == 0:
            return calc_ways(left_index)

        left_ways = calc_ways(left_index)
        right_ways = calc_ways(right_index)

        total_size = left_size + right_size

        combination = math.comb(total_size, left_size) % MOD
        combination_ = combination * left_ways % MOD
        combination__ = combination_ * right_ways % MOD

        return combination__

    return calc_ways(0) - 1

def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        return sum(map(lambda n : n - minimum, nums))

"""
The algorithm that will equalize the list in the least number of steps is as
follow:
> At each step, increment all but the maximum value by 1



Consider the following formula:
`total_gap nums = sum $ map ((min nums) -) nums`
This value decrease by one for each operation. And when it reaches 0, the list
is equalized.
So the number of steps required is simply sum(map(lambda n : n - minimum, nums))
"""

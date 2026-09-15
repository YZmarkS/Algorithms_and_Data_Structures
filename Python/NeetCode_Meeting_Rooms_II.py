from collections import deque

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

a = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
b = [Interval(4, 9)]
c = [Interval(0, 8), Interval(8, 10)]

def minMeetingRooms(intervals: List[Interval]) -> int:
    max_room = 0
    room = 0
    starts = deque(sorted(list(map(lambda interval : interval.start, intervals))))
    ends = deque(sorted(list(map(lambda interval : interval.end, intervals))))
    while starts:
        next_start = starts[0]
        next_end = ends[0]
        if next_start < next_end:
            room += 1
            starts.popleft()
        else: # next_end <= next_start:
            room -= 1
            ends.popleft()
        max_room = max(max_room, room)

    return max_room

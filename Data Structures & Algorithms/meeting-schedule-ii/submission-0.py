"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # max_end = max(interval[1] for interval in intervals)
        max_end = max(interval.end for interval in intervals)

        difference_arr = [0] * (max_end + 1)

        for interval in intervals:
            difference_arr[interval.start] += 1
            difference_arr[interval.end] -= 1
        
        max_count = 0
        room_count = 0

        for time in difference_arr:
            room_count += time
            max_count = max(max_count, room_count)
        
        return max_count


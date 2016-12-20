# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        head = []
        index = 0
        while index < len(intervals):
            interval = intervals[index]
            index += 1
            if interval.end < newInterval.start:
                head.append(interval)
            else:
                if interval.start <= newInterval.start:
                    newInterval.start = interval.start
                break
        index = len(intervals) - 1
        tail = []
        while index >= 0:
            interval = intervals[index]
            index -= 1
            if interval.start > newInterval.end:
                tail.append(interval)
            else:
                if interval.end >= newInterval.end:
                    newInterval.end = interval.end
                break
        tail.reverse()
        result = head + [newInterval] + tail
        return result
            
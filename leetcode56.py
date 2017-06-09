# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        sort_interval = sorted(intervals, key=lambda x: x.start)
        result = [sort_interval[0]]
        for i, item in enumerate(sort_interval[1:]):
            if item.start <= result[-1].end:
                result[-1] = Interval(result[-1].start, max(item.end, result[-1].end))
            else:
                result.append(item)
        return result
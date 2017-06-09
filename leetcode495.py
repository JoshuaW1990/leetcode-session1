class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = 0
        if timeSeries == []:
            return 0
        for i, time in enumerate(timeSeries[:-1]):
            result += min(duration,, timeSeries[i+1]-time)
        result += duration
        return result
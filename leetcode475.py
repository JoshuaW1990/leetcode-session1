class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        i, rad = 0, 0
        for house in sorted(houses):
            while house >= sum(heaters[i:i+2]) / 2.0:
                i += 1
            rad = max(rad, abs(heaters[i] - house))
        return rad

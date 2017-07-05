class Solution(object):
    def mySqrt(self, x):
        """
        Use binary search here
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        while low <= high:
            mid = (low + high) / 2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                high = mid - 1
            else:
                low = mid + 1
        return high

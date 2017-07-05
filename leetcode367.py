class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 0, num
        while low <= high:
            mid = (low + high) / 2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                high = mid - 1
            else:
                low = mid + 1
        if low**2 != num and high**2 != num:
            return False
        else:
            return True

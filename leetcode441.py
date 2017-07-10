class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        level = 0
        count = level
        while count <= n:
            level += 1
            count += level
        return level - 1


"""
http://bookshadow.com/weblog/2016/10/30/leetcode-arranging-coins/
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(2 * n + 0.25) - 0.5)


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l <= r:
            m = (l + r) / 2
            if m * (m + 1) / 2 > n:
                r = m - 1
            else:
                l = m + 1
        return r

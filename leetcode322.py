"""
my code: DP
"""
import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        DP = [amount + 1 for i in xrange(amount + 1)]
        DP[0] = 0
        for num in xrange(1, amount + 1):
            for coin in coins:
                if coin <= num:
                    DP[num] = min(DP[num], DP[num - coin] + 1)
        if DP[-1] == amount + 1:
            return -1
        else:
            return DP[-1]

"""
BFS: https://discuss.leetcode.com/topic/32589/fast-python-bfs-solution/3
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        level = seen = {0}
        number = 0
        while level:
            if amount in level:
                return number
            level = {a+c for a in level for c in coins if a+c <= amount} - seen
            seen |= level
            number += 1
        return -1
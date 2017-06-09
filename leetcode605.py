"""
Description:
You cannot change the position of the plants which has been in the flowerbed.

"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        result = 0
        for i, num in enumerate(flowerbed):
            if num == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                        flowerbed[i] = 1
                        result += 1
        return result >= n
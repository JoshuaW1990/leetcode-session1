class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxList = []
        for num in nums:
            if num in maxList:
                continue
            if len(maxList) == 0 or num > maxList[0]:
                maxList.insert(0, num)
            elif len(maxList) == 1 or maxList[0] > num > maxList[1]:
                maxList.insert(1, num)
            elif len(maxList) == 2 or maxList[1] > num > maxList[2]:
                maxList.insert(2, num)
            maxList[:] = maxList[:3]
        if len(maxList) < 3:
            return maxList[0]
        else:
            return maxList[2]

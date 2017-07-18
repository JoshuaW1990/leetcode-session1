class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortNum = sorted(nums)
        sortNum.reverse()
        sortDict = {}
        for i, num in enumerate(sortNum):
            sortDict[num] = i
        ans = []
        for num in nums:
            rank = sortDict[num]
            if rank == 0:
                ans.append('Gold Medal')
            elif rank == 1:
                ans.append('Silver Medal')
            elif rank == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(rank + 1))
        return ans

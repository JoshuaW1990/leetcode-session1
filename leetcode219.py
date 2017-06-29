class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = dict()
        for i, num in enumerate(nums):
            if num not in numDict:
                numDict[num] = i
            else:
                if i - numDict[num] <= k:
                    return True
                else:
                    numDict[num] = i
        return False

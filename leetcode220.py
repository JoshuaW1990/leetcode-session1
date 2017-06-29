class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        def myCmp(item1, item2):
            if item1[0] < item2[0]:
                return -1
            elif item1[0] == item2[0]:
                return 0
            else:
                return 1


        newNums = [(num, index) for index, num in enumerate(nums)]
        newNums.sort(cmp=myCmp)
        i = 0
        while i < len(newNums):
            prevNum, prevIndex = newNums[i]
            j = i + 1
            while j < len(newNums):
                currentNum, currentIndex = newNums[j]
                if currentNum - prevNum > t:
                    break
                if abs(prevIndex - currentIndex) <= k:
                    return True
                j += 1
            i += 1
        return False


"""
http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >=  k:
                numDict.popitem(last=False)
        return False

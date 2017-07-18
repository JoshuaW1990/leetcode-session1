class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        nums.sort()
        maxLength = 0
        index = 1
        currentNumber = nums[0]
        currentLength = 1
        prevNumber = None
        prevLength = 0
        while index < len(nums):
            if nums[index] == currentNumber:
                currentLength += 1
            else:
                if prevNumber is not None and currentNumber - prevNumber == 1:
                    maxLength = max(maxLength, currentLength + prevLength)
                prevNumber, prevLength = currentNumber, currentLength
                currentNumber, currentLength = nums[index], 1
            index += 1
        if prevNumber is not None and currentNumber - prevNumber == 1:
            maxLength = max(maxLength, currentLength + prevLength)
        return maxLength


"""
Use hash
"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        counter = dict()
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        maxLength = 0
        keys = counter.keys()
        keys.sort()
        for i in xrange(1, len(keys)):
            prevNum = keys[i - 1]
            currentNum = keys[i]
            if currentNum - prevNum == 1:
                maxLength = max(maxLength, counter[prevNum] + counter[currentNum])
        return maxLength

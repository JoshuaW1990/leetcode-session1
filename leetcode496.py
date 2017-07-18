class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nextDict = dict()
        queue = []
        for num in nums:
            nextDict[num] = -1
            newQueue = []
            for current in queue:
                if num > current:
                    nextDict[current] = num
                else:
                    newQueue.append(current)
            queue = newQueue + [num]

        ans = []
        for num in findNums:
            ans.append(nextDict[num])
        return ans



"""
With stack: http://bookshadow.com/weblog/2017/02/05/leetcode-next-greater-element-i/
"""
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dmap = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dmap[stack.pop()] = n
            stack.append(n)
        return [dmap.get(n, -1) for n in findNums]

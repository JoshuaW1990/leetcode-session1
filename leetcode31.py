class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 0:
            index = len(nums) - 1
            subList = []
            while index > 0:
                subList.append(nums[index])
                if nums[index] > nums[index - 1]:
                    break
                index -= 1
            if index == 0:
                nums.reverse()
            else:
                subList.sort()
                for i in xrange(len(subList)):
                    if subList[i] > nums[index - 1]:
                        nums[index - 1], subList[i] = subList[i], nums[index - 1]
                        break
                nums[index:] = subList[:]

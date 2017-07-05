class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = slow = 0
        while fast < len(nums):
            nums[slow] = nums[fast]
            fast += 1
            slow += 1
            if fast < len(nums) and nums[fast] == nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            while fast < len(nums) and nums[fast] == nums[fast - 1]:
                fast += 1
        return slow
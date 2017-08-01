class Solution(object):
    def threeSum(self, nums):
        """
        Here we use two pointers algorithm for two sum
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in xrange(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] < -nums[i]:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return ans

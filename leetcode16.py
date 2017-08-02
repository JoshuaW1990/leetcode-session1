class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = None
        minDiff = float('inf')
        nums.sort()
        for i in xrange(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    diff = target - (nums[left] + nums[right] + nums[i])
                    if abs(diff) < minDiff:
                        ans = nums[left] + nums[right] + nums[i]
                        minDiff = abs(diff)
                    if diff == 0:
                        return ans
                    elif diff > 0:
                        left += 1
                    else:
                        right -= 1
        return ans

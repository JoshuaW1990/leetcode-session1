class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, nums):
        # write your code here
        # equation is: curMax = max(curMax, idx + nums[idx])
        lastMax, curMax, njumps, idx = 0, 0, 0, 0
        while lastMax < len(nums) - 1:
            while idx <= lastMax:
                curMax = max(curMax, idx + nums[idx])
                idx += 1
            if lastMax == curMax:
                return -1
            lastMax = curMax
            njumps += 1
        return njumps

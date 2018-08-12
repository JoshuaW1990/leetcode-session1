class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # http://www.cnblogs.com/zuoyuan/p/3777496.html
        n=len(nums)
        for i in range(n):
            if nums[i]<=0: 
                nums[i]=n+2
        for i in range(n):
            if abs(nums[i])<=n:
                curr=abs(nums[i])-1
                nums[curr]=-abs(nums[curr])
        for i in range(n):
            if nums[i]>0: return i+1
        return n+1
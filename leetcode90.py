class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resList = [()]
        for num in sorted(nums):
            resList += [tuple(list(item) + [num]) for item in resList]
        resSet = set(resList)
        ans = []
        for item in resSet:
            ans.append(list(item))
        return ans


"""
Use DFS
http://www.cnblogs.com/zuoyuan/p/3758346.html
"""
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, nums):
        def dfs(depth, start, valuelist):
            if valuelist not in res: res.append(valuelist)
            if depth == len(nums): return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, valuelist+[nums[i]])
        nums.sort()
        res = []
        dfs(0, 0, [])
        return res

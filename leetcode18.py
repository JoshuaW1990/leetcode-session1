class Solution(object):
    def fourSum(self, nums, target):
        """
        Starts from the 3Sum approach
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # http://www.cnblogs.com/zuoyuan/p/3699384.html
        sumDict = {}
        result = set()
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                tmpSum = nums[i] + nums[j]
                if tmpSum not in sumDict:
                    sumDict[tmpSum] = [(i, j)]
                else:
                    sumDict[tmpSum].append((i, j))
                if target - tmpSum in sumDict:
                    for item in sumDict[target - tmpSum]:
                        if i in item or j in item:
                            continue
                        tmp = sorted([nums[i], nums[j], nums[item[0]], nums[item[1]]])
                        result.add(tuple(tmp))
        ans = []
        for item in result:
            ans += [list(item)]
        return ans


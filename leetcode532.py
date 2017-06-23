class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        counter = dict()
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        count = 0
        for num in counter.keys():
            current_num = num + k
            if current_num not in counter:
                continue
            else:
                if k == 0:
                    if counter[current_num] > 1:
                        count += 1
                else:
                    count += 1
        return count

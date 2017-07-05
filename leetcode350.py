class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter = dict()
        for num in nums1:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        ans = []
        for num in nums2:
            if num not in counter:
                continue
            else:
                counter[num] -= 1
                ans.append(num)
                if counter[num] == 0:
                    del counter[num]
        return ans

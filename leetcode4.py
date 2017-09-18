class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # use merge: O(m + n)
        def merge(ar1, ar2):
            res = []
            ptr1 = ptr2 = 0
            while ptr1 < len(nums1) and ptr2 < len(nums2):
                if nums1[ptr1] < nums2[ptr2]:
                    res.append(nums1[ptr1])
                    ptr1 += 1
                else:
                    res.append(nums2[ptr2])
                    ptr2 += 1
            if ptr1 == len(nums1):
                res.extend(nums2[ptr2:])
            else:
                res.extend(nums1[ptr1:])
            return res
        
        nums = merge(nums1, nums2)
        mid = len(nums) / 2
        if len(nums) % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2.0
        else:
            return nums[mid]
        


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """   
        # use binary-search: O(log(m + n))
        def getKth(A, B, k):
            lenA = len(A)
            lenB = len(B)
            if lenA > lenB:
                return getKth(B, A, k)
            if lenA == 0:
                return B[k-1]
            if k == 1:
                return min(A[0], B[0])
            ptrA = min(k/2, lenA)
            ptrB = k - ptrA
            if A[ptrA - 1] <= B[ptrB - 1]:
                return getKth(A[ptrA:], B, ptrB)
            else:
                return getKth(A, B[ptrB:], ptrA)
        
        lenA = len(nums1)
        lenB = len(nums2)
        if (lenA + lenB) % 2 == 1:
            return getKth(nums1, nums2, (lenA + lenB) / 2 + 1)
        else:
            return (getKth(nums1, nums2, (lenA + lenB) / 2) + getKth(nums1, nums2, (lenA + lenB) / 2 + 1)) / 2.0
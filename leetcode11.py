class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            minHeight = min(height[left], height[right])
            width = right - left
            ans = max(ans, width * minHeight)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return ans
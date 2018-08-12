class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start_index, end_index = 0, len(height) - 1
        if len(height) <= 2:
            return 0

        for i in xrange(end_index + 1):
            if i == end_index:
                return 0
            if height[i] > height[i + 1]:
                start_index = i
                break
        for i in xrange(end_index, start_index - 1, -1):
            if i == start_index:
                return 0
            if height[i] > height[i - 1]:
                end_index = i
                break

        def singleTrap(heightList):
            if len(heightList) < 3:
                return 0
            if len(heightList) == 3:
                maxNum = heightList[1]
                maxIndex = 1
            else:
                maxNum = max(heightList[1:-1])
                maxIndex = heightList[1:-1].index(maxNum) + 1
            if maxNum >= heightList[0] or maxNum >= heightList[-1]:
                return singleTrap(heightList[:maxIndex + 1]) + singleTrap(heightList[maxIndex:])
            smallPeak = min(heightList[0], heightList[-1])
            result = 0
            for num in heightList[1:-1]:
                result += smallPeak - num
            return result

        return singleTrap(height[start_index : end_index + 1])

print "success"



# second session
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        maxHeight = max(height)
        left = 0
        right = len(height) - 1
        currentHeight = 0
        water = 0
        while height[left] < maxHeight:
            if height[left] > currentHeight:
                currentHeight = height[left]
            else:
                water += currentHeight - height[left]
            left += 1
        currentHeight = 0
        while height[right] < maxHeight:
            if height[right] > currentHeight:
                currentHeight = height[right]
            else:
                water += currentHeight - height[right]
            right -= 1
        if left == right:
            return water
        for i in xrange(left, right):
            water += maxHeight - height[i]
        return water

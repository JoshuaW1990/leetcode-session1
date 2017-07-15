class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area)) + 1
        while w > 0:
            l = area / w
            if l * w == area and l >= w:
                return [l, w]
        return None

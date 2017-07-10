class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x1, y1 in points:
            distanceMap = collections.defaultdict(int)
            for x2, y2 in points:
                dist = (x2 - x1)**2 + (y2 - y1)**2
                if dist == 0:
                    continue
                distanceMap[dist] += 1
            for dist in distanceMap.keys():
                ans += distanceMap[dist] * (distanceMap[dist] - 1)
        return ans

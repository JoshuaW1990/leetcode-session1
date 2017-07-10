class Solution(object):
    def findContentChildren(self, g, s):
        """
        Time: O(mn)
        result: TLE

        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        ans = 0
        for greed in g:
            minSize = float('inf')
            index = -1
            for i, size in enumerate(s):
                if size < greed:
                    continue
                if size < minSize:
                    minSize = size
                    index = i
            if index == -1:
                continue
            else:
                ans += 1
                del s[index]
        return ans




class Solution(object):
    def findContentChildren(self, g, s):
        """
        Time: O(min(NlogN, MlogM))


        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        indexG, indexS = 0, 0
        ans = 0
        while indexG < len(g) and indexS < len(s):
            while indexS < len(s) and s[indexS] < g[indexG]:
                indexS += 1
            if indexS == len(s):
                break
            else:
                ans += 1
                indexG += 1
                indexS += 1
        return ans

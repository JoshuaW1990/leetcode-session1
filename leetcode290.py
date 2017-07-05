class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        patternList = list(pattern)
        strList = str.split(' ')
        if len(patternList) != len(strList):
            return False
        sourceMap, targetMap = dict(), dict()
        for i in xrange(len(patternList)):
            source = sourceMap.get(strList[i], None)
            target = targetMap.get(patternList[i], None)
            if source is None and target is None:
                sourceMap[strList[i]] = patternList[i]
                targetMap[patternList[i]] = strList[i]
            elif source != patternList[i] or target != strList[i]:
                return False
        return True

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strDict = {}
        for word in strs:
            sortWord = ''.join(sorted(word))
            if sortWord in strDict:
                strDict[sortWord].append(word)
            else:
                strDict[sortWord] = [word]
        return strDict.values()

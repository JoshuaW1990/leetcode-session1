class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        ans = []
        for word in words:
            wordSet = set(word.lower())
            if len(wordSet) == len(wordSet & set1) or len(wordSet) == len(wordSet & set2) or len(wordSet) == len(wordSet & set3):
                ans.append(word)
        return ans

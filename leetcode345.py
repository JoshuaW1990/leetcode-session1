class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        start, end = 0, len(s) - 1
        sList = list(s)
        while start < end:
            while start < end and sList[start] not in vowels:
                start += 1
            while start < end and sList[end] not in vowels:
                end -= 1
            sList[start], sList[end] = sList[end], sList[start]
            start += 1
            end -= 1
        return ''.join(sList)

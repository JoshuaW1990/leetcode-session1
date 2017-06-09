class Solution(object):
    def isAnagram(self, s, t):
        """
        Use hash table here to count the frequency of the characters in a word and check it with another word.


        :type s: str
        :type t: str
        :rtype: bool
        """
        ch_dict = {}
        for ch in s:
            if ch not in ch_dict:
                ch_dict[ch] = 1
            else:
                ch_dict[ch] += 1

        for ch in t:
            if ch not in ch_dict:
                return False
            else:
                ch_dict[ch] -= 1
                if ch_dict[ch] == 0:
                    del ch_dict[ch]

        return len(ch_dict) == 0
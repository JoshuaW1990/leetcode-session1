"""
Use hash map
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ch_dict = {}
        for ch in ransomNote:
            if ch not in ch_dict:
                ch_dict[ch] = 1
            else:
                ch_dict[ch] += 1
        for ch in magazine:
            if ch not in ch_dict:
                continue
            else:
                ch_dict[ch] -= 1
                if ch_dict[ch] == 0:
                    del ch_dict[ch]
        return len(ch_dict) == 0
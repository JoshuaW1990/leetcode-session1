from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counter1 = Counter(s1)
        counter2 = Counter(s2[:len(s1) - 1])
        for i in xrange(len(s1) - 1, len(s2)):
            counter2[s2[i]] += 1
            if counter1 == counter2:
                return True
            counter2[s2[i - len(s1) + 1]] -= 1
            if counter2[s2[i - len(s1) + 1]] == 0:
                del counter2[s2[i - len(s1) + 1]]
        return counter1 == counter2
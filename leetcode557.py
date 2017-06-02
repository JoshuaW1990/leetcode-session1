class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split(' ')
        for i, string in enumerate(slist):
            if string == '':
                del slist[i]
            else:
                slist[i] = string[::-1]
        return ' '.join(slist)

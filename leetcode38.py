class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current = '1'
        while n > 1:
            prev = current
            current = ''
            for i in xrange(len(prev) + 1):
                if i == 0:
                    ch = prev[i]
                    count = 1
                elif i == len(prev):
                    current += str(count) + ch
                else:
                    if ch == prev[i]:
                        count += 1
                    else:
                        current += str(count) + ch
                        ch = prev[i]
                        count = 1
            n -= 1
        return current

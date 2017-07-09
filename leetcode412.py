class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in xrange(1, n + 1):
            item = ''
            if i % 3 == 0:
                item += 'Fizz'
            if i % 5 == 0:
                item += 'Buzz'
            if item == '':
                item = str(i)
            ans.append(item)
        return ans

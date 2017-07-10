class Solution(object):
    def createPalindrome(self, num):
        return int(num + num[::-1])

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        high = 10**n - 1
        low = high / 10

        for num in xrange(high, low, -1):
            palindrome = self.createPalindrome(str(num))
            for i in xrange(high, low, -1):
                if palindrome / i > high:
                    break
                if palindrome % i == 0:
                    return (palindrome % 1337)
        return -1

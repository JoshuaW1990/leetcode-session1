class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [sys.maxint] * n
        ptr = [0] * len(primes)
        dp[0] = 1
        for i in xrange(1, n):
            dp[i] = min([dp[ptr[idx]] * primes[idx] for idx in range(len(primes))])
            for k in range(len(primes)):
                if dp[i] == dp[ptr[k]] * primes[k]:
                    ptr[k] += 1
        return dp[-1]

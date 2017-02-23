class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        # return False if the length of s1 and s2 not equal to s3
        if l1 + l2 != l3:
        	return False
        # Initialize the dp table with False
        dp = [[False for _ in xrange(l2 + 1)] for _ in xrange(l1 + 1)]
        for i in xrange(l1 + 1):
        	for j in xrange(l2 + 1):
        		# If both s1 and s2 are empty string
        		if i == 0 and j == 0:
        			dp[i][j] = True
        		# If s1 is empty
        		elif i == 0 and s2[j - 1] == s3[j - 1]:
        			dp[i][j] = dp[i][j - 1]
        		# If s2 is empty
        		elif j == 0 and s1[i - 1] == s3[i - 1]:
        			dp[i][j] = dp[i - 1][j]
        		# If the current character in s3 only matches s1
        		elif s1[i - 1] == s3[i + j - 1] and s2[j - 1] != s3[i + j - 1]:
        			dp[i][j] = dp[i - 1][j]
        		# If the current character in s3 only matches s2
        		elif s1[j - 1] != s3[i + j - 1] and s2[j - 1] == s3[i + j - 1]:
        			dp[i][j] = dp[i][j - 1]
        		# If the current character in s3 matches both of s1 and s2
        		elif s1[i - 1] == s3[i + j - 1] and s2[j - 1] == s3[i + j - 1]:
        			dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[-1][-1]
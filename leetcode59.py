class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        # https://www.hrwhisper.me/leetcode-spiral-matrix-or-spiral-matrix-ii/
        ans = [[0 for x in range(n)] for x in range(n)]
        row, cnt, tot = (n >> 1) + 1, 1, n * n
        for k in range(row):
            i = k
            while i < n - k and cnt <= tot:
                ans[k][i] = cnt
                i, cnt = i + 1, cnt + 1
            i = k + 1
            while i < n - k and cnt <= tot:
                ans[i][n - k - 1] = cnt
                i, cnt = i + 1, cnt + 1
            i = n - k - 2
            while i >= k and cnt <= tot:
                ans[n - k - 1][i] = cnt
                i, cnt = i - 1, cnt + 1
            i = n - k - 2
            while i > k and cnt <= tot:
                ans[i][k] = cnt
                i, cnt = i - 1, cnt + 1
        return ans

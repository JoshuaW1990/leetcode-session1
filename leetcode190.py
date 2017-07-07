class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_str = list(bin(n))[2:]
        binary_str.reverse()
        length = len(binary_str)
        num_zero = 32 - length
        binary_str = binary_str + ['0'] * num_zero
        num = ''.join(binary_str)
        return int(num, 2)



"""
Second session
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = format(n, 'b').zfill(32)[::-1]
        return int(ans, 2)

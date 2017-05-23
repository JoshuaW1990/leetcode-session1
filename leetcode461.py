class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
		stringX = format(x, 'b').zfill(32)
		stringY = format(y, 'b').zfill(32)
		distance = 0
		for i, chX in enumerate(stringX):
			chY = stringY[i]
			if chX != chY:
				distance += 1
		return distance
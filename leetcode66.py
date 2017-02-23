class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            digits[-1] = 0
            # there is no digits before that
            if len(digits) == 1:
                return [1, 0]
            else:
                return self.plusOne(digits[:-1]) + [0]

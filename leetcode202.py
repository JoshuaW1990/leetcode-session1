class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        number = n
        while number not in visited:
            number = sum([int(num)**2 for num in list(str(number))])
            if number == 1:
                return True
            else:
                visited.add(number)
        return False

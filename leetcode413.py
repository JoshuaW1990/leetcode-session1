class Solution(object):
    def calculateNum(self, n):
        # n: length of the list
        # return the total number of the sublist with length more than 2
        """
        length      total number      
        3               1               
        4               3           
        5               6
        equation result = (n - 1)(n - 2) / 2
        """
        return ((n - 1) * (n - 2) / 2)
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # use the list to store the length of each arithmetic sequence, then calculate the total number for each one and sum them together
        if len(A) < 3:
            return 0
        # obtain the length of the arthmetic sequence
        sublist_length = []
        difference = A[1] - A[0]
        count = 2
        for i in xrange(2, len(A)):
            if A[i] - A[i - 1] == difference:
                count += 1
            else:
                if count > 2:
                    sublist_length.append(count)
                count = 2
                difference = A[i] - A[i - 1]
        if count > 2:
            sublist_length.append(count)
        # calculate the length for each arithmetic sequence
        result = 0
        for num in sublist_length:
            result += self.calculateNum(num)
        return result
        

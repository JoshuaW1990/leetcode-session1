class Solution(object):
    minPay = float('inf')
    def filter(self, spList, needs):
        result = []
        for sp in spList:
            i = 0
            while i < len(needs):
                if sp[i] > needs[i]:
                    break
                i += 1
            if i == len(needs):
                result.append(sp)
        return result

    def helper(self, price, available, needs, pays):
        if len(available) == 0:
            for i, item in enumerate(price):
                pays += needs[i] * item
            if pays < self.minPay:
                self.minPay = pays
            return
        for item in available:
            target = [needs[i] - item[i] for i in xrange(len(needs))]
            newAvailable = self.filter(available, target)
            self.helper(price, newAvailable, target, pays + item[-1])



    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        available = self.filter(special, needs)
        pay2 = sum([price[i] * needs[i] for i in xrange(len(needs))])
        self.helper(price, available, needs, 0)
        return min(pay2, self.minPay)

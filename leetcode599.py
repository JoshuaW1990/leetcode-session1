class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1, dict2 = dict(), dict()
        for i, name in enumerate(list1):
            dict1[name] = i
        set1 = set(dict1.keys())
        for i, name in enumerate(list2):
            dict2[name] = i
        set2 = set(dict2.keys())
        commenSet = set1 & set2
        minIndex = float('inf')
        minName = []
        for name in commenSet:
            if dict1[name] + dict2[name] < minIndex:
                minName = [name]
                minIndex = dict1[name] + dict2[name]
            elif dict1[name] + dict2[name] == minIndex:
                minName.append(name)
            else:
                continue
        return minName

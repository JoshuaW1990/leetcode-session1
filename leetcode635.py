class LogSystem(object):

    def __init__(self):
        self.array = []
        self.sort = False


    def search(self, timestamp):
        start, end = 0, len(self.array)
        while start < end:
            mid = (start + end) / 2
            if self.array[mid][1] == timestamp:
                return mid
            elif self.array[mid][1] > timestamp:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        # if len(self.array) == 0:
        #     self.array.append((id, timestamp))
        #     return
        # index = self.search(timestamp)
        # if id == 16:
        #     print "index = ", index
        # self.array = self.array[:index] + [(id, timestamp)] + self.array[index:]
        # # self.array.insert(index, (id, timestamp))
        self.array.append((id, timestamp))
        self.sort = False

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        def myCmp(item1, item2):
            if item1[1] < item2[1]:
                return -1
            elif item1[1] == item2[1]:
                return 0
            else:
                return 1


        constStart = ':00:00:00:00:00'
        constEnd = ':12:31:23:59:59'
        if gra == 'Year':
            s = s[:4] + constStart
            e = e[:4] + constEnd
        elif gra == 'Month':
            s = s[:7] + constStart[3:]
            e = e[:7] + constEnd[3:]
        elif gra == 'Day':
            s = s[:10] + constStart[6:]
            e = e[:10] + constEnd[6:]
        elif gra == 'Hour':
            s = s[:13] + constStart[9:]
            e = e[:13] +constEnd[9:]
        elif gra == 'Minute':
            s = s[:16] + constStart[12:]
            e = e[:16] + constEnd[12:]

        if not self.sort:
            self.array.sort(cmp=myCmp)
            self.sort = True

        startIndex = self.search(s)
        endIndex = self.search(e)
        while 0 <= startIndex < len(self.array) and self.array[startIndex][1] >= s:
            startIndex -= 1
        if startIndex == -1:
            startIndex += 1
        while 0 <= startIndex < len(self.array) and self.array[startIndex][1] < s:
            startIndex += 1
        while 0 <= endIndex < len(self.array) and self.array[endIndex][1] > e:
            endIndex -= 1
        if endIndex == -1:
            endIndex = 0
        while 0 <= endIndex < len(self.array) and self.array[endIndex][1] <= e:
            endIndex += 1

        result = []
        for item in self.array[startIndex:endIndex]:
            result.append(item[0])
        return result







# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

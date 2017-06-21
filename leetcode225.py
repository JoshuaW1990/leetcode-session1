class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.topItem = None


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self.topItem = x


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queue == []:
            return None
        tmpQueue = []
        self.topItem = None
        while len(self.queue) > 1:
            self.topItem = self.queue.pop(0)
            tmpQueue.append(self.topItem)
        result = self.queue[0]
        self.queue = tmpQueue
        return result



    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topItem



    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        return self.outStack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (self.inStack == []) and (self.outStack == [])

    def move(self):
        """
        Move the items from inStack to outStack
        """
        if self.outStack == []:
            while self.inStack:
                self.outStack.append(self.inStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Problem: Implement Queue Using Stacks - https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue(object):

    def __init__(self):
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)
        return self.list

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return "the stack is empty"
        else:
            num = self.list[0]
            self.list.remove(self.list[0])
            return num

    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return "the stack is empty"
        else:
            return self.list[0]


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.list) == 0:
            return True
        else:
            return False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
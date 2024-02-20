from sortedcontainers import SortedList

class MinStack:
    def __init__(self):
        self.stack = []
        self.sorted = SortedList()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.sorted.add(val)


    def pop(self) -> None:
        num = self.stack.pop()
        self.sorted.remove(num)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return  self.sorted[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
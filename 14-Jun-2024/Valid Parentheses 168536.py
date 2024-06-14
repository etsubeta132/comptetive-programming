# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Stack:
    def __init__(self):
        self.list = []

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        openningP = "{[("
        closingP = ")]}"
        if len(s) == 1 or s[0] in closingP:
            return False
        else:
            for i in s:
                if i in openningP:
                    stack.push(i)
                elif i in closingP:
                    if stack.isEmpty():
                        return False
                    else:
                        if i == ")" and stack.peek() == "(" or i == "]" and stack.peek() == "[" or i == "}" and stack.peek() == "{":
                            stack.pop()
                        else:
                            return False
            return stack.isEmpty()
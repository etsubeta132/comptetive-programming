# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def validate(s):
            stack = []
            for i in s:
                if i == "#":
                    if stack: stack.pop()
                else: stack.append(i)
            return "".join(stack)
        
        return validate(s) == validate(t)
        
                
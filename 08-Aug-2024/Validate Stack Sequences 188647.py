# Problem: Validate Stack Sequences - https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = r = 0
        stack = []

        while l < len(pushed) and r < len(popped):
            stack.append(pushed[l])
            l += 1
            while stack and stack[-1] == popped[r]:
                stack.pop()
                r += 1
        
        return not stack

            
            


        
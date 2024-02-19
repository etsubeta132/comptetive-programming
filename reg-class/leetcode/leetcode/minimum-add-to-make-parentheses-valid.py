class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for p in s:
            if p == ")":
                if stack:
                    stack.pop()
                else:
                    res+=1
            else:
                stack.append(p)

        return res+len(stack)
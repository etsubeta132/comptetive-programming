# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while stack and k > 0 and stack[-1] > ch:
                k -= 1
                stack.pop()
            stack.append(ch)
        while stack and k > 0:
            stack.pop()
            k -= 1
        ans = "".join(stack)
        i = 0
        while i < len(ans) and ans[i] == '0':
            i += 1
        if i == len(ans):
            return "0"
        return ans[i:]
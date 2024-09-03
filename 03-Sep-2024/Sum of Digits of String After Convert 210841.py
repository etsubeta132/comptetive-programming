# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        sm = ""
        for i in s:
            sm += str(ord(i) - ord("a")  + 1)
        
        sm = int(sm)
        for i in range(k):
            s = 0
            while sm >= 1:
                s += (sm % 10)
                sm = sm // 10
            sm = s
        
        return sm
        
            


            
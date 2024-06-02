# Problem: Shifting Letters - https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shift = [0]*len(s)
        shift[-1] = (shifts[-1]) % 26
        shifted_s = []
        
        for i in range(len(s) - 2, -1, -1):
            shift[i] += (shifts[i] + shift[i + 1]) % 26
            
        for i, char in enumerate(s):

            idx = ord(char) + shift[i]
         
            if idx > ord("z"):
                idx = (idx - ord("z")) + ord("a") - 1
            
            shifted_s.append(chr(idx))
        
        return "".join(shifted_s)


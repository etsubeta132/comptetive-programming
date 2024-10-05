# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        xor = start ^ goal
        bitFlip = 0

        while xor:
            xor &= (xor - 1)
            bitFlip += 1
        
        return bitFlip
        
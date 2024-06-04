# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = bin(n)[2:]

        for i in range(len(bit) - 1):
            if bit[i] == bit[i + 1]:
                return False
                
        return True
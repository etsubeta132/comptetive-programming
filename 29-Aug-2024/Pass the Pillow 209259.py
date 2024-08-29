# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        que = time // (n - 1)

        if que % 2 == 0:
            return (time % (n - 1) + 1)
        else:
            return (n - time % (n - 1))

       

    
        
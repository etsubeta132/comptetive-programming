# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        dice = len(rolls) + n
        n_tot = (mean * dice) - sum(rolls)
        each_dice = n_tot / n
        if each_dice > 6 or each_dice < 1:
            return []
        else:
            n_rolls = [1] * n
            val = n_tot - n
            l = 0
            while val > 0 and l < n:
                mx = min(5, val)
                n_rolls[l] += mx
                val -= mx
                l += 1
            return n_rolls


        


        
# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        ctr_b = 0
        ctr_a = s.count("a")

        ans = ctr_a + ctr_b
        for i in s:
            if i == "a":
                ctr_a -= 1
            else:
                ctr_b += 1
            
            ans = min(ctr_a + ctr_b, ans)

        return ans

                



        
        



# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        
        ctr = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                ctr += 1
        
        return ctr
# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        substring = set()
        
        min_num_substring = 1
        for i in range(len(s)):
            if s[i] in substring:
                min_num_substring += 1
                substring = set()

            substring.add(s[i])
        
        return min_num_substring
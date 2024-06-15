# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        MAX_VAL = 100000
        
        freq = [0] * (MAX_VAL + 1)
        
        maxNum = 0
        totalIncrements = 0
        nextAvailable = -1
        
        for num in nums:
            freq[num] += 1
            maxNum = max(num, maxNum)
        
        for num in range(maxNum + 1):
            if freq[num] != 0:
                diff = max(0, nextAvailable + 1 - num)
                count = freq[num]
                
                totalIncrements += diff * count + (count * (count - 1)) // 2
                
                nextAvailable = max(nextAvailable + 1, num) + count - 1
        
        return totalIncrements
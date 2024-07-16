# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        bag = [1]*numOnes + [0]*numZeros + [-1]*numNegOnes
        res = 0
        l = 0
        ctr = 0
        while ctr < k:
            res+=bag[ctr]
            ctr+=1
        
        return res
        


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        total = int(n * (n + 1) / 2)

        num_sum = sum(nums)
       
        missed = total - num_sum

        return missed




        
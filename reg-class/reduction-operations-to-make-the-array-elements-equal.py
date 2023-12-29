class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

    
        nums.sort(reverse = True)
        curr = None
        ctr = 0
        for idx,val in enumerate(nums):
            if curr != val:
                curr = val
                ctr+=idx
                
        return ctr 
         


        

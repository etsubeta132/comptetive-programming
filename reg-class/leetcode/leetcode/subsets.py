class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(idx):
            if idx >= len(nums):
                result.append(subset[:])
                return 
            
            # decide to include num[idx]
            subset.append(nums[idx])
            backtrack(idx + 1)

            # decide not to inclde nums[idx]
            subset.pop()
            backtrack(idx+1)

        backtrack(0)
        
        return result
        


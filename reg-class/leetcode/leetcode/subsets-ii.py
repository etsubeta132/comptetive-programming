class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []
        def backtrack(idx):
            if idx >= len(nums):
                sub = sorted(subset)
                if sub not in result:
                    result.append(sub)
                return
            
            subset.append(nums[idx])
            backtrack(idx+1)

            subset.pop()
            backtrack(idx+1)
        
        backtrack(0)
        result.sort()
        
        
        return result

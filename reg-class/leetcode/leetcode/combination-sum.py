class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        subset = []

        def backtrack(idx):
            if sum(subset) >= target:
                if sum(subset) == target:
                    result.append(subset[:])
                return
 
            
            for i in range(idx , len(candidates)):
                subset.append(candidates[i])
                backtrack(i)
                subset.pop()
    
            
        backtrack(0)

        return result
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(idx):
            if len(subset) == k:
                result.append(subset[:])
                return 
            
            for i in range(idx,n):
                subset.append(i+1)
                backtrack(i+1)
                subset.pop()
            
        backtrack(0)
        return result
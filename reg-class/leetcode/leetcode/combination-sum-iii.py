class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        sub = []
        def bactrack(idx):
            if len(sub) >= k or sum(sub) >= n:
                if sum(sub) == n and  len(sub) == k:
                    result.append(sub[:])
                return 

            for i in range(idx,10):
                sub.append(i)
                bactrack(i+1)
                sub.pop()
            
            return result
        bactrack(1)
        return result
        
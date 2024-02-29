class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        sub = []
        res = 0
        def backtrack(idx,res):
            if res >= target:
                if res == target:
                    result.append(sub[:])
                return 
            
            if idx >= len(candidates):
                return result
            
            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue 
                if candidates[i]>target:
                    break           
                sub.append(candidates[i])
                res+=candidates[i]
                backtrack(i+1,res)

                n = sub.pop()
                res-=n
            return result
        
        candidates.sort()
        backtrack(0,0)

        return result


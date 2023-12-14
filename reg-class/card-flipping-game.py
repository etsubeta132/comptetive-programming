class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        d = {}
        for i in range(len(fronts)):
            d[fronts[i]] = True
            d[backs[i]] = True

        for j in range(len(fronts)):
            if fronts[j] == backs[j]:
                d[fronts[j]] = False

        ans  = float('inf')
        for i in range(len(fronts)):
            if d[fronts[i]]:
                ans = min(ans, fronts[i])

            if d[backs[i]]:
                ans   = min(ans, backs[i])
        

        return ans if ans < float('inf') else 0 


        
        

                






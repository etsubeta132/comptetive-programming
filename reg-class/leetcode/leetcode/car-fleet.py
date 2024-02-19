class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        idx = sorted(range(len(position)), key = lambda i : position[i],reverse= True)
        position.sort(reverse= True)
        pre = 0
        for i in range(len(position)):
            j = idx[i]
            tm = (target-position[i])/speed[j]
            if tm > pre:
                pre = tm
                ans+=1
            
        return ans


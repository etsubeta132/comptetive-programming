class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = sorted(costs,key = lambda x:x[0]-x[1])
        n = len(costs)//2
        res=0
        for i in range(n):
            res+=cost[i][0]
        for i in range(n,2*n):
            res+=cost[i][1]

        return res
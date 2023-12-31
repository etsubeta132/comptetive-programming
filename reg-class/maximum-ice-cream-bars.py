class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx = max(costs)
        cost = [0]*(mx+1)
        
        for i in costs:
            cost[i] = cost[i]+1


        sorted_costs = []
        l = 0
        while l < len(cost):
            sorted_costs.extend([l]*cost[l])
            l+=1
        
        bars = 0
        r = 0
        while bars < coins and r < len(sorted_costs):
            bars+=sorted_costs[r]
            if bars > coins:
                return r
            else:
                r+=1
        return r


            
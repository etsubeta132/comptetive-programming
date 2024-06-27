# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_diff = [(prof, diff) for prof, diff in zip(profit, difficulty)]
        profit_diff.sort(reverse = True)
    
        worker.sort(reverse = True)
        
        total_profit = 0
        for ability in worker:
            for prof, diff in profit_diff:
                if diff <= ability:
                    total_profit += prof
                    break
        
        return total_profit
            




        
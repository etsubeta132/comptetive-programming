# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employe = defaultdict(list)

        for d, mgr in enumerate(manager):
            employe[mgr].append(d)
        
        def dfs(mgr):
            
            res = informTime[mgr]
            for emp in employe[mgr]:
                res = max(res, informTime[mgr] + dfs(emp))
            
            return res
        
        return  dfs(headID)



       
        

            


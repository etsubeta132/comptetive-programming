# Problem: Minimum Time to Collect All Apples in a Tree - https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
       
        adj = [[] for _ in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(i, par):
            temp = 0
            for child in adj[i]:
                if(child != par):
                    temp += dfs(child, i)
            if((temp>0 or hasApple[i]) and par != -1):
                temp += 2
            return temp
            
        return dfs(0, -1)
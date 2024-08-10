# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key =  lambda  x: x[2])
        queries = [queries[i] + [i] for i in range(len(queries))]
        queries.sort(key =  lambda  x: x[2])

        parent_dict = {i:i for i in  range(n)}
        rank = {i:0 for i in range(n)}


        def find(x):
            while x != parent_dict[x]:
                x = parent_dict[x]
            
            return x
        
        def union(x, y):

            parent1 = find(x)
            parent2 = find(y)

            if parent1 != parent2:
                if rank[parent1] > rank[parent2]:
                    parent_dict[parent2] = parent1
                elif rank[parent2] > rank[parent1]:
                    parent_dict[parent1] = parent2
                else:
                    parent_dict[parent2] = parent1
                    rank[parent1] += 1 
        
        result = [True]*len(queries)
        l = 0

        for query in queries:

            while l < len(edgeList) and edgeList[l][2] < query[2]:
                edge = edgeList[l]
                union(edge[0], edge[1])
                l += 1
                
                if l < len(edgeList):
                    edge = edgeList[l]
                
            
            if find(query[0]) == find(query[1]):
                result[query[3]] = True
            else:
                result[query[3]] = False
        
        return result

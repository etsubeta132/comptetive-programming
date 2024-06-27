# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = {i : i for i in range(n)}
        rank = {i :0 for i in range(n)}

        def find(x):

            if x == parent[x]:
                return x
            
            return find(parent[x])
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx 
                elif rank[rooty] > rank[rootx]:
                    parent[rootx] = rooty
                else:
                    parent[rooty] = rootx
                    rank[x] += 1

        for x, y in edges:
            union(x, y)
        
        components = defaultdict(int)
        for key, val in parent.items():
            node = find(val)
            components[node] += 1
        
        ans = []
        sm =  0
        values = [val for val in components.values()]

        for val in values:
            ans.append(sm * val)
            sm += val
        
        return sum(ans)





            
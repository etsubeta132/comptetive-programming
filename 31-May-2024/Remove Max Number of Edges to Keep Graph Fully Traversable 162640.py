# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = {i+1:i+1 for i in range(n)}
        bob = {i+1:i+1 for i in range(n)}

        rankA = {i+1:0 for i in range(n)}
        rankB = {i+1:0 for i in range(n)}

        def find(u, parent):
            while u != parent[u]:
                u = parent[u]
            
            return u
        
        def union(u, v, parent, rank):
            rootu = find(u, parent)
            rootv = find(v, parent)

            if rootu != rootv:

                if rank[rootu] > rank[rootv]:
                    parent[rootv] = rootu

                elif rank[rootv] > rank[rootu]:
                    parent[rootu] = rootv
            
                else:
                    parent[rootu] = rootv
                    rank[rootv] += 1
            
        
        edges.sort(reverse = True)
        edge_removed = 0

        for edge in edges:
            ty, u, v = edge

            if ty == 1:
                if find(u, alice) == find(v, alice):
                    edge_removed += 1
                else:
                    union(u, v, alice, rankA)
            elif ty == 2:
                if find(u, bob) == find(v, bob):
                    edge_removed += 1
                else:
                    union(u, v, bob, rankB)
            else:
                if find(u, bob) == find(v, bob) and find(u, alice) == find(v, alice):
                    edge_removed += 1
                else:
                    union(u, v, bob, rankB)
                    union(u, v, alice, rankA)
                    
    
        bob_set = set()
        alice_set = set()

        for node, parent in bob.items():
            par = find(parent, bob)
            bob_set.add(par)
        
        for node, parent in alice.items():
            par = find(parent, alice)
            alice_set.add(par)
        
        isTraversible = len(bob_set) == len(alice_set) == 1

        return edge_removed if isTraversible else -1
        


            
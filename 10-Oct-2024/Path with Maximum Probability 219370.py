# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph, deq = defaultdict(list), deque([start])
        
        for idx, edge in enumerate(edges):
            x, y = edge
            graph[x].append((y, idx))
            graph[y].append((x, idx))
            
        probs = [0] * n
        probs[start] = 1
        
        while deq:
            node = deq.popleft()
                
            for child, idx in graph[node]:
                if probs[node] * succProb[idx] > probs[child]:
                    probs[child] = probs[node] * succProb[idx]
                    deq.append(child)
        return probs[end]
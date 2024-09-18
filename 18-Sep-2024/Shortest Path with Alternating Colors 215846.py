# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        redAdjList = defaultdict(list)
        blueAdjList = defaultdict(list)

        for a, b in blueEdges:
            blueAdjList[a].append(b)
        
        for a, b in redEdges:
            redAdjList[a].append(b)
        
        queue = deque([(0, "b"), [0, "r"]])
        result = {i: -1 for i in range(1, n)}
        result[0] = 0
        visited = set()

        level = 0
        while queue:
            ln = len(queue)

            for i in range(ln):
                node, color = queue.popleft()
                
                if result[node] == -1:
                    result[node] = level
                
                if color == "r":
                    for neigh in blueAdjList[node]:
                        if (neigh, "b") not in visited:
                            queue.append((neigh, "b"))
                            visited.add((neigh, "b"))
                else:
                    for neigh in redAdjList[node]:
                        if (neigh, "r") not in visited:
                            queue.append((neigh, "r"))
                            visited.add((neigh, "r"))
           
            level += 1
        
        ans = [-1] * n
        for node, val in result.items():
            ans[node] = val

        return ans



    
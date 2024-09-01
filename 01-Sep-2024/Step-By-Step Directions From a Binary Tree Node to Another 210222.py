# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        graph = defaultdict(list)
        
        def buildGraph(root):
            if root == None:
                return
            
            if root.left:
                graph[root.val].append((root.left.val, "L"))
                graph[root.left.val].append((root.val, "U"))
            
            if root.right:
                graph[root.val].append((root.right.val, "R"))
                graph[root.right.val].append((root.val, "U"))
            
            buildGraph(root.left)
            buildGraph(root.right)
        
        buildGraph(root)
        queue = deque([(startValue, "")])
        visited = set([startValue])

        
        while queue:
            ln = len(queue)
            node, path = queue.popleft()
            visited.add(node)
            
            for child, pt in graph[node]:
                if child not in visited:
                    if child == destValue:
                        return path + pt
                    new_path = path + pt
                                    
                    queue.append((child, new_path))
        
     
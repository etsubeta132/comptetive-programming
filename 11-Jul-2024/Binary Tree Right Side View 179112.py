# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []

        stack = [(root)]
        res = []
        while stack:
            for i in range(len(stack)):
                n = stack.pop(0)
                if n.left: stack.append(n.left)
                if n.right: stack.append(n.right)
            
            res.append(n.val)

        return res
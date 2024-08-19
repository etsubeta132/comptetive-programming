# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root,sm):
            if not root:
                return False
            
            sm += root.val

            if not root.left and not root.right:
                return targetSum == sm
            
            ans = dfs(root.left,sm) or dfs(root.right,sm)

            return ans
        
        return dfs(root,0)
            
        
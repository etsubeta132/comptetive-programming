# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root, mini, maxi):
            if not root: return True

            if root.val >= maxi or root.val <= mini: return False

            return check(root.left, mini, root.val) and check(root.right, root.val, maxi)

        return check(root, -inf, inf)


            
        

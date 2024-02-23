# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None
        
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        
        bigTree = TreeNode(v1+v2)
        
        if not root1:return root2
        elif not root2:return root1
        
        bigTree.left = self.mergeTrees(root1.left if root1.left else None, root2.left if root2.left else None)  
        bigTree.right = self.mergeTrees(root1.right if root1.right else None,root2.right if root2.right else None)

        return bigTree


            




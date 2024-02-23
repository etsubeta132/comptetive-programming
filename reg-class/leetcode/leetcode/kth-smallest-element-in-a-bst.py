# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res =[]
        def Traverse(root):
            if not root:
                return res
            
            if len(res) == k:
                return res
            
            Traverse(root.left)

            res.append(root.val)

            Traverse(root.right)
        

        Traverse(root)
        
        return res[k-1]
        
            

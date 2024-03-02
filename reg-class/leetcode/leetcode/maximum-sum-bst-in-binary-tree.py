# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        def search(root):
            if not root:
                return True,float('inf'),float('-inf'),0
            
            left_bst,lmin,lmax,lsum = search(root.left)
            right_bst,rmin,rmax,rsum = search(root.right)

            if left_bst and right_bst and lmax < root.val <rmin:
                subtree_sum = lsum+rsum +root.val
                nonlocal result
                result = max(result,subtree_sum)

                return True, min(lmin,root.val),max(rmax,root.val),subtree_sum
            
            return False,0,0,0

        result = 0
        search(root)

        return result
        
            

        
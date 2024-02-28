# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def maxdiff(root,mn,mx):
            if not root:
                return 0
            
            self.result = max(self.result,abs(mn - root.val),abs(mx - root.val))

            mn = min(mn,root.val)
            mx = max(mx,root.val)
            
            maxdiff(root.left,mn,mx)
            maxdiff(root.right,mn,mx)

        maxdiff(root,root.val,root.val)

        return self.result

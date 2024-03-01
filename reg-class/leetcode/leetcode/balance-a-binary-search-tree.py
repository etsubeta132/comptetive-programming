# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []
        def getNodes(root):
            if not root:
                return 
            
            getNodes(root.left)
            res.append(root.val)
            getNodes(root.right)
        
        getNodes(root)
        res.sort()

        def build(start,end):
            mid = (start+end)//2
            if start > end:
                return 
            
            node = TreeNode(res[mid])
            node.left = build(start,mid-1)
            node.right = build(mid+1,end)

            return node
        
        return build(0,len(res)-1)


        
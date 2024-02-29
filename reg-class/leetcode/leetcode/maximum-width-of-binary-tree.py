# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        width = defaultdict(list)
        if not root:
            return -1
        else:
            width[0].append(1)
            
        def getChild(root,s,w):
            if not root:
                return 
            
            if root.left:
                width[s+1].append(2*w)
                getChild(root.left,s+1,2*w)
            
            if root.right:
                width[s+1].append((2*w)+1)
                getChild(root.right,s+1,(2*w)+1)
            return width
        
        getChild(root,0,1)
        mx_width = 0
        for i in width.keys():
            mx_width = max(mx_width,max(width[i]) - min(width[i])+1)
        return mx_width
            
            
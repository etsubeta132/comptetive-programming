# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        output = []
        if not root:
            return output
        else:
           output = [[root.val]] 
        
        
        def getChild(parent,child):
            if parent == 0:
                return child
            
            for p in parent:
                if p.left:
                    child.append(p.left)
                if p.right:
                    child.append(p.right)
            return child
        
        child = getChild([root],[])
        reverse = True
        while child !=[]:
            out = []
            for ch in child:
                out.append(ch.val)
            if reverse:
                output.append(out[::-1])
                reverse = False
            else:
                output.append(out)
                reverse = True
            
            child = getChild(child,[])
        
        return output

            

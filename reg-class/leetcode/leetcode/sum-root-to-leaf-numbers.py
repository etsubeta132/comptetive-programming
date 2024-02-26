# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root,0)]
        res = []
        out = []
        while stack:
            p,l = stack.pop()
            print(p.val,l,out)
            if not (p.left or p.right):
                ans = "".join(out[:l])+str(p.val)
                res.append(ans)
            else:
                out = out[:l]+[str(p.val)]
                if p.left:
                    stack.append((p.left,l+1))

                if p.right:
                    stack.append((p.right,l+1))
        
        tot = 0
        for num in res:
            tot+=int(num)
            
        return tot



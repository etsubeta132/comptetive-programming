# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def search(root):
            if not root:
                return None
            
            search(root.left)
            count[root.val] += 1
            search(root.right)
        
        search(root)
        mx = max(count.values())
        res = []
        for k,v in count.items():
            if v == mx:
                res.append(k)
        return res
        
            


from sortedcontainers import SortedList
# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mydict=defaultdict(SortedList)
        def helper(node,r,c):
            if not node:
                return None
            mydict[c].add((r,node.val))
            helper(node.left,r+1,c-1)
            helper(node.right,r+1,c+1)
        helper(root,0,0)

        sorted_dict = dict(sorted(mydict.items()))
        res = []
        for key,val in sorted_dict.items():
            out = [i[1] for i in val]
            res.append(out)
        
        return res
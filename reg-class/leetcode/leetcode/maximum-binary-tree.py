# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        mxdict = {nums[i]:i for i in range(len(nums))}
        def build(start,end):
            if start >= end:
                return 
            
            val = max(nums[start:end])
            idx = mxdict[val]

            node = TreeNode(val)
            node.left = build(start,idx)
            node.right = build(idx+1,end)
            
            return  node
        
        return build(0,len(nums))
# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(node):
            if node == None:
                return 0
            
            robChild = dp(node.left) + dp(node.right)
            robParent = node.val

            if node.left:
                leftChild = node.left
                robParent += dp(leftChild.left) + dp(leftChild.right)

            if node.right:
                rightChild = node.right
                robParent += dp(rightChild.left) + dp(rightChild.right)

            return max(robChild, robParent)
        
        return dp(root)

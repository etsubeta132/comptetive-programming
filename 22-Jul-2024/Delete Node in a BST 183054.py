# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def searchAndDelete(root,key):
            if not root:
                return None
            
            if key < root.val:
                root.left = searchAndDelete(root.left,key)
            elif key > root.val:
                root.right = searchAndDelete(root.right,key)
            else:
                if not root.left: return root.right
                elif not root.right: return root.left

                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = searchAndDelete(root.right,root.val)
            return root
        return searchAndDelete(root,key)
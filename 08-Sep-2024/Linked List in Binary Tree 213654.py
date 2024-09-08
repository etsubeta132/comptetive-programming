# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        result = []
        res = []
        def dfs(node, res):
            if not node.left and not node.right:
                result.append("#".join(res))
                return
            if res == []:
                res.append(str(node.val))
            if node.left:
                res.append(str(node.left.val))
                dfs(node.left, res)
                res.pop()
            
            if node.right:
                res.append(str(node.right.val))
                dfs(node.right, res)
                res.pop()
            
            return
        result2 = []
        while head:
            result2.append(str(head.val))
            head = head.next
        
        dfs(root, res)
        
        result2 = "#".join(result2)
        for res in result:
            if result2 in res:
                return True
        
        return False
            

            
            
            
        
# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = deque([root])
        
        while queue:
            # get the length of each level
            ln = len(queue)
            
            # iterate through elements in each level
            for i in range(ln):
                node = queue.pop()
                if i != ln - 1:
                    node.next = queue[-1]
                    
                if node.left:
                    queue.appendleft(node.left)
                    
                if node.right:
                    queue.appendleft(node.right)
        
        return root   

        
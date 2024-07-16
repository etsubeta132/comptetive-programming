# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        root = ListNode()
        tail = root
        while head:
            ans = 0
            while head and head.val != 0:
                ans += head.val
                head = head.next
            
            while head and head.val == 0:
                head = head.next
            
            if ans != 0:
                tail.next = ListNode(ans)
                tail = tail.next
        
        return root.next
            
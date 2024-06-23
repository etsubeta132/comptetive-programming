# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        tail = head
        next = head.next
        head.next = None

        while next:
            node = next
            next = next.next
            node.next = None

            temp =  tail
            tail = node
            tail.next = temp
        
        return tail




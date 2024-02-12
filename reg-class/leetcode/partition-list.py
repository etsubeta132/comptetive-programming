# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greater = ListNode()
        nextless = less
        nextgreater = greater

        while head:
            if head.val >= x:
                nextgreater.next = head
                nextgreater = nextgreater.next
            else:
                nextless.next = head
                nextless = nextless.next
            
            head = head.next
        
        
        greater = greater.next
        nextless.next = greater
        nextgreater.next = None
        less = less.next

        return less


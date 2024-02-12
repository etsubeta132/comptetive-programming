# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        ahead,back = dummy,dummy
        
        for i in range(n):
            ahead = ahead.next
        
        while ahead and ahead.next:
            ahead = ahead.next
            back = back.next
        
        if back.next:
            back.next = back.next.next

        return dummy.next
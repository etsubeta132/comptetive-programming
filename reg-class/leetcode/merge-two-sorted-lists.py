# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        merged = ListNode()
        sorted = merged

        while left and right:
            if left.val<=right.val:
                sorted.next = left
                left = left.next
            else:
                sorted.next = right
                right = right.next
            
            sorted = sorted.next
        
        if left:
            sorted.next = left
            left = left.next

        if right:
            sorted.next = right
            right = right.next
            
        return merged.next
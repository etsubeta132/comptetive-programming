# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tail = node = ListNode()
        while head:
            prev = head.val
            head = head.next
            if head and head.val == prev:
                while head and head.val == prev: 
                    head = head.next
               
            else:
                node.next = ListNode(prev)
                node = node.next
                    
        return tail.next
        
            
            
        
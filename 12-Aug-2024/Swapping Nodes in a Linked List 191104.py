# Problem: Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = head
        r = head
        count = head
        ctr = 0
        while count:
            ctr += 1
            count = count.next

        p = 0
        while l and p < k - 1:
            l = l.next
            p += 1
        
        p = 0
        while r and p < ctr - k:
            r = r.next
            p += 1
        
        if l and r:
            l.val, r.val = r.val,l.val
        
        return head
        



        
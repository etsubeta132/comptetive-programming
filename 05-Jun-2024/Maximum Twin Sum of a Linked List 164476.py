# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        half_nodes = []
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            half_nodes.append(slow.val)
            slow = slow.next
        res = 0
        for i in range(len(half_nodes)-1,-1,-1):
            res = max(res,half_nodes[i]+ slow.val)
            slow = slow.next
        
        return res



        
         
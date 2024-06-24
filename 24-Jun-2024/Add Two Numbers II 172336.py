# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1 
        prev = None
        while cur:
            hold = cur.next
            cur.next = prev
            prev = cur
            cur = hold
        l1 = prev

        cur = l2 
        prev = None
        while cur:
            hold = cur.next
            cur.next = prev
            prev = cur
            cur = hold
        l2 = prev
        dummy = ListNode(0)
        cur = dummy
        num1 = l1
        num2 = l2
        rem = 0
        while l1 and l2:
            new = ListNode((l1.val + l2.val + rem) % 10)
            rem =int(l1.val + l2.val + rem > 9)
            cur.next = new
            cur = cur.next

            l1 = l1.next
            l2 = l2.next
        while l1:
            new = ListNode((l1.val + rem) % 10)
            rem =int(l1.val + rem > 9)
            cur.next = new
            cur = cur.next

            l1 = l1.next
        while l2:
            new = ListNode((l2.val + rem) % 10)
            rem =int(l2.val + rem > 9)
            cur.next = new
            cur = cur.next

            l2 = l2.next
        if rem:
            new = ListNode(rem)
            cur.next = new
            cur = cur.next
        dummy = dummy.next
        cur = dummy 
        prev = None
        while cur:
            hold = cur.next
            cur.next = prev
            prev = cur
            cur = hold
        return prev

        
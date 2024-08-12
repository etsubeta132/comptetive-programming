# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

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
    
        def sortList(left,right,sorted):
            if left and right:
                if left.val<=right.val:
                    sorted.next = left
                    left = left.next
                else:
                    sorted.next = right
                    right = right.next
            elif left:
                sorted.next = left
                left = left.next
            elif right:
                sorted.next = right
                right = right.next
            else:
                return merged.next
            
            sorted = sorted.next

            return sortList(left,right,sorted)

        return sortList(left,right,sorted)
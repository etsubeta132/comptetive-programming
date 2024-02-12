# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        
        oddNode = head
        evenNode = head.next
        

        while oddNode and evenNode:
            even = oddNode.next
            if evenNode.next:
                oddNode.next = evenNode.next
                oddNode = evenNode.next
            

                odd = oddNode.next
                oddNode.next = even

                evenNode.next = odd
                evenNode = odd
            else:
                return head

        return head
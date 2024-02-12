# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodesA = set()

        while headA:
            nodesA.add(headA)
            headA = headA.next
            
        while headB:
            if headB in nodesA:
                return headB

            headB = headB.next
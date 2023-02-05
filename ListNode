# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dum=cur=ListNode()
        carry=0
        while l1 or l2:
            d=carry
            if l1 and l2:
                d+=(l1.val+l2.val)
                l1=l1.next
                l2=l2.next
            elif l1:
                d+=l1.val
                l1=l1.next
            elif l2:
                d+=l2.val
                l2=l2.next
            carry=d//10
            cur.next=ListNode(d%10)
            cur=cur.next
        if carry ==1:
            cur.next=ListNode(1)
        return dum.next

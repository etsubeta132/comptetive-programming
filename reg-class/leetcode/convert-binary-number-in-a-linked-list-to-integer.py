# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        101 =5 => 4+0+1
        1010 = 10 => 8+0+2+0
        """
        ctr = 0
        counter = head
        while counter:
            ctr+=1
            counter = counter.next
        value = 0
        
        ctr-=1
        while head:
            value +=(int(head.val)*(2**ctr))
            head = head.next
            ctr-=1
        
        return value


        
        
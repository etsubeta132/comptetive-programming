# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        output = ListNode()
        output.next = head
        node = output
        
        while(node):
            first = node.next
            second = None
            if first:
                second = first.next
            if second:
                secondNext = second.next
                second.next = first
                node.next = second
                first.next = secondNext
                node = first
            else:
                break
        return output.next

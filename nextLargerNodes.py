# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        ans = []
        mon = []
        cur = head
        i = 0
        while cur:
            ans.append(0)
            while mon and cur.val > mon[-1][0]:
                val, idx = mon.pop()
                ans[idx] = cur.val
            mon.append((cur.val, i))
            i += 1
            cur = cur.next
        return ans

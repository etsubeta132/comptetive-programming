# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        counter = head
        pholder = []
        ctr = 0
        while counter:
            ctr+=1
            pholder.append(counter.val)
            counter = counter.next
        
        sp = ctr//k
        r = ctr%k
        start = 0
        splits  = []
        for i in range(k):

            end = start+sp-1
            if r > 0:
                end = start+sp
            split = ListNode()
            pointer = split
            while start < end+1:
                pointer.next = head
                pointer = pointer.next
                head = head.next
                start+=1
            split = split.next
            pointer.next = None
            splits.append(split)
            start = end+1
            r-=1
        
        return splits
         

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        
        l,r = left,right
        while l < r:
            nums[l-1],nums[r-1] = nums[r-1],nums[l-1]
            l+=1
            r-=1
    
        rev = head 
        l = 0
        while rev and l < right:
            rev.val = nums[l]
            l+=1
            rev = rev.next
        
        return head
            


    




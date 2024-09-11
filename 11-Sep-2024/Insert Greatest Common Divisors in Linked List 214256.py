# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a 

    def insertGreatestCommonDivisors(self, head):
        ans = ListNode(0)  
        cur = ans  

        while head.next:
            gcd_val = self.gcd(head.val, head.next.val)  
            
            cur.next = ListNode(head.val)  
            cur.next.next = ListNode(gcd_val) 
            
            head = head.next
            cur = cur.next.next 

        cur.next = ListNode(head.val)  
        
        return ans.next 
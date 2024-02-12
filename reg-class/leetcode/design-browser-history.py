class Node:
    def __init__(self,val='', next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(val = homepage)
        self.tail = Node(val = homepage)
        


    def visit(self, url: str) -> None:
        
        page = Node(url)

        if not self.head.next:
            temp = self.head.next
            self.head.next = page
            page.prev = self.head
        
        page.prev  = self.tail
        self.tail.next = page
        self.tail = page


    def back(self, steps: int) -> str:
        while self.tail.prev and steps > 0:
            self.tail = self.tail.prev
            steps-=1
        
        if self.tail:
            return self.tail.val
        

    def forward(self, steps: int) -> str:
        
        while self.tail.next and steps > 0:
            self.tail = self.tail.next
            steps-=1
        
        if self.tail:
            return self.tail.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
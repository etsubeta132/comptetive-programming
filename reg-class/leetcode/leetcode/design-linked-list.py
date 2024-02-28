class MyLinkedList:

    def __init__(self):
        self.head = []
        
    def get(self, index: int) -> int:
        if index > len(self.head) - 1:
            return -1
        
        return self.head[index]
        
    def addAtHead(self, val: int) -> None:
        self.head.insert(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.head.append(val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < len(self.head):
            self.head.insert(index, val)
        elif index == len(self.head):
            self.head.append(val)
        
    def deleteAtIndex(self, index: int) -> None:
        if index > len(self.head) - 1:
            return
        
        self.head.pop(index)
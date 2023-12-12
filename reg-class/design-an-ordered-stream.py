class OrderedStream:

    def __init__(self, n: int):
        self.os = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.os[idKey] = value
        ans = []
        id = idKey
        is_sorted = True
        for i in range(1,id):
            if i not in self.os:
                is_sorted = False
        
        if is_sorted:
            while id in self.os:
                ans.append(self.os[id])
                id+=1
            return ans
        else:
            return []
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
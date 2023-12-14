class Bitset:

    def __init__(self, size: int):
        self.bitset = {i:0 for i in range(size)}
        self.reversebit = {i:1 for i in range(size)}

        self.ctr_1 = 0
        self.ctr_0 = 0


    def fix(self, idx: int) -> None:
        if self.bitset[idx] == 0:
            self.bitset[idx] = 1
            self.ctr_1+=1
        
        if self.reversebit[idx] == 1:
            self.reversebit[idx] = 0
            self.ctr_0+=1


    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == 1:
            self.bitset[idx] = 0
            self.ctr_1 -=1

        if self.reversebit[idx] == 0:
            self.reversebit[idx] = 1
            self.ctr_0 -=1

        

    def flip(self) -> None:
        l = len(self.bitset)
        self.ctr_1 = l-self.ctr_1
        self.ctr_0 = l-self.ctr_0

        
        self.bitset , self.reversebit = self.reversebit, self.bitset


    def all(self) -> bool:

        return self.ctr_1 == len(self.bitset)
        

    def one(self) -> bool:

        if self.ctr_1 >= 1:
            return True
        else:
            return False
        

    def count(self) -> int:

        return self.ctr_1

    def toString(self) -> str:

        bit = []

        for val in self.bitset.values():
            bit.append(str(val))
        
        bit = "".join(bit)
        
        return bit
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
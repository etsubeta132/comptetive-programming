class RandomizedSet:

    def __init__(self):
        self.randomset = set()
        

    def insert(self, val: int) -> bool:

        if val in self.randomset:
            was_in = True
        else:
            was_in = False
            self.randomset.add(val)

        return not was_in

        

    def remove(self, val: int) -> bool:

        if val in self.randomset:
            was_in = True
            self.randomset.remove(val)
        else:
            was_in = False


        return was_in

    def getRandom(self) -> int:

        return random.choice(list(self.randomset))
        
       

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class ATM:

    def __init__(self):
        
        self.banknotes = [0] * 5
        self.notes = [20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
     
        self.banknotes = [a+b for a,b in zip(self.banknotes,banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        handed_notes = [0] * 5
        
        for i in range(4,-1,-1):
            handed_notes[i] = min(self.banknotes[i],amount //self.notes[i])
            amount-= handed_notes[i] * self.notes[i]
            
        if amount == 0:
            self.banknotes = [a-b for a,b in zip(self.banknotes,handed_notes)]
            return handed_notes
        else:     
            return [-1]
 
        return handed_notes
        
            

            


        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
class UndergroundSystem:

    def __init__(self):
        self.checkin = defaultdict(tuple)
        self.checkout = defaultdict(list)
        

        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName,t]

        


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,time = self.checkin[id]
        total = t-time
        self.checkout[(start,stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        travel = self.checkout[(startStation,endStation)]

        total_time  = sum(travel)
        total_travler = len(travel)

        return total_time/total_travler

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
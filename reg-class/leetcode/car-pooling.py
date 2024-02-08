class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        
        mx = 0
        for trip in trips:
            mx = max(trip[2],mx)
        
        seats = [0]*(mx+2)
        
        for trip in trips:
            k,l,r = trip[0],trip[1],trip[2]
            
            seats[l]+=k
            seats[r]-=k
        
        for i in range(1,mx):
            seats[i] += seats[i-1]
        
        cap = max(seats)
        return True if cap <= capacity else False
            
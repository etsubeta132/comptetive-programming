class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0]*(n+1)

        for book in bookings:
            l,r,k = book[0],book[1],book[2]
            seats[l-1]+=k
            seats[r]-=k
        
        for i in range(1,n):
            seats[i] += seats[i-1]
        
        return seats[:-1]
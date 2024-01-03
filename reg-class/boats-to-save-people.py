class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l,r = 0, len(people)-1
        ctr = 0

        while l <= r:
            weight = people[l]+people[r]

            if weight <= limit:
                l+=1
            
            ctr+=1
            r-=1
        
        return ctr




class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int: 

        cw = 0
        anticw = 0
        idx = start
        print(distance,start,destination)
        while idx != destination:
            cw+=distance[idx]
            idx+=1
            if idx==len(distance):
                idx=0
            print(idx,cw)

        while idx != start:
            anticw+=distance[idx]
            idx+=1
            if idx==len(distance):
                idx=0
            print(idx,anticw)
        
        short_distance = min(cw,anticw)
        return short_distance
        
        
        
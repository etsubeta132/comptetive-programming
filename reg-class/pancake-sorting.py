class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        idx = {arr[i]:i for i in range(len(arr))}

        p = len(arr)-1
        opp = []
       
        
        while p >= 0 :
            mx = max(arr[:p+1])
            i = arr.index(mx)

            if  i != p:

                opp.append(i+1)

                arr = arr[:i+1][::-1] + arr[i+1:]

                opp.append(p+1)

                arr = arr[:p+1][::-1] + arr[p+1:]
                
            p-=1
        
        return opp
            


                




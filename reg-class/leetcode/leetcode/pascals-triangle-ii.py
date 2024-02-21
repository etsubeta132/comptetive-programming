class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res  = []
        def sumUp(res):
            if len(res) ==0:
                return [1]
            
            if len(res)==1:
                return [1,1]
            
            ans = [1,1]
            l,r = 0,1
            
            while r < len(res):
                ans.insert(l+1,res[l]+res[r])
                r+=1
                l+=1
            
            return ans
        
        res =[1]
        while rowIndex > 0:
            res = sumUp(res)
            rowIndex-=1

        return res

            

         

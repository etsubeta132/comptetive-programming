class Solution:
    def smallestNumber(self, num: int) -> int:

        isneg = False

        if num < 0:
            isneg=True
            num= str(num*-1)
        else:
            num= str(num)      
        num = [str(num[i]) for i in range(len(num))]

        num.sort()
        
        if isneg:
            num = num[::-1]
            return int("".join(num))*-1
        else:
            
            if num[0] == "0" and len(num)>1:
                l = 1
                while num[l] == "0":
                    l+=1

                num[0],num[l] = num[l],num[0]
            
            return int("".join(num))
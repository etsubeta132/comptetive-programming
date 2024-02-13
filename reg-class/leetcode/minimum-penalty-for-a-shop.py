class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n =  len(customers) + 1
        p = []
        s = [0]*n

        r = 0
        for i in range(n-1):
            p.append(r)
            if customers[i] == "N":
                r += 1
        p.append(r)
    
        t = 0
        for j in range(n-2, -1, -1):
            if customers[j] == "Y":
                t += 1
            s[j] = t

        mn = 0
        result = [p[0]+s[0]]
        for i in range(1,n):
            rs =  p[i]+s[i]
            if rs < result[mn]:
                mn = i
            result.append(rs)

        return mn 


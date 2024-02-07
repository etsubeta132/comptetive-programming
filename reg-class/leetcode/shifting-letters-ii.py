class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lett = list(map(ord,s))
        prefList = [0]*(len(s)+1)
        new_s = []
        for shift in shifts:
            l,r = shift[0],shift[1]
            forward = shift[2]

            if forward:
                prefList[l]+=1
                prefList[r+1]-=1
            else:
                prefList[l]+= -1
                prefList[r+1]-= -1

        sm = 0
        for i in range(len(s)):
            sm+=prefList[i]
            new_c = chr((((lett[i] + sm) - 97 ) % 26 ) + 97)
            new_s.append(new_c)
        
        return "".join(new_s)

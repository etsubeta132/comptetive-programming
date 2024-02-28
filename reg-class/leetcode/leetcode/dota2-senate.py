class Solution:
    def predictPartyVictory(self, senate):

        qr,qd = deque(),deque()
        for i,c in enumerate(senate):
            if c == "D": qd.append(i)
            else: qr.append(i)
        
        while qr and qd:
            r,d  = qr.popleft(),qd.popleft()

            if r < d: qr.append(d+len(senate))

            else:  qd.append(r+len(senate))
        
        return "Radiant" if qr else "Dire"



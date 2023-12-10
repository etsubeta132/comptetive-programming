class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
       
        win_lose = {}
        lose_one = []
        lose_none = []

        for player in matches:
            if player[0] in win_lose:
                win_lose[player[0]][0] +=1 
            else:
                win_lose[player[0]] = [1,0]
        
            if player[1] in win_lose:
                win_lose[player[1]][1] +=1 
            else:
                win_lose[player[1]] = [0,1]
        
        

        for key,value in win_lose.items():
            if value[1]==0:
                 lose_none.append(key)
            elif value[1] == 1:
                lose_one.append(key)

        lose_none.sort()
        lose_one.sort()
        return [lose_none,lose_one]


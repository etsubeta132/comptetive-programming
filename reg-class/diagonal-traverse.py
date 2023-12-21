class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        result = []
        reverse = False

        for i in range(len(mat)):
            dig_list = []
            r = i
            c = 0
            while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
                dig_list.append(mat[r][c])
                r-=1
                c+=1

            if reverse:
                result.extend(dig_list[len(dig_list)-1::-1])
                reverse = False
            else:
                result.extend(dig_list)
                reverse = True
        
        for j in range(1,len(mat[0])):
            
            dig_list = []
            r = len(mat)-1
            c = j
            while 0 <= r < len(mat) and 0 <= c < len(mat[0]):
                dig_list.append(mat[r][c])
                r-=1
                c+=1

            if reverse:
                result.extend(dig_list[len(dig_list)-1::-1])
                reverse = False
            else:
                result.extend(dig_list)
                reverse = True

        return result





        
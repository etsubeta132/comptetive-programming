class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            l,r = 0,len(image[0])-1
            while l<r:
                image[i][l],image[i][r] = image[i][r],image[i][l]
                l+=1
                r-=1

            for j in range(len(image[i])):
                if image[i][j] == 0:
                     image[i][j] = 1
                else:
                    image[i][j] = 0
        
        return image
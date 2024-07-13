# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dir = [(-1, -1), (-1, 0), (0, 0), (1, 0), (0, -1), (0, 1), (1, 1),(-1, 1), (1, -1)]
        smoothed = [[0] * len(img[0]) for i in range(len(img))]
            
        for i in range(len(img)):
            for j in range(len(img[0])):
                ctr = 0
                total = 0
                for r, c in dir:
                    if 0 <= i + r < len(img) and 0 <= j + c < len(img[0]):
                        ctr += 1
                        total += img[r+i][j+c]
                
                smoothed[i][j] = math.floor(total / ctr)
        
        return smoothed 
                




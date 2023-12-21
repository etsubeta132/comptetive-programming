class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        ctr  = Counter(nums)

        zeros_l = 0
        ones_r = ctr[1]
        max_div  = max(0,zeros_l+ones_r)
        max_div_list = [0]
        
        for i in range(1,len(nums)+1):

            if nums[i-1] == 0:
                zeros_l += 1
            
            elif nums[i-1] == 1:
                ones_r -= 1
     
            curr_div = zeros_l+ones_r
            
            if max_div == curr_div:
               max_div_list.append(i) 

            elif max_div < curr_div:
                max_div = curr_div
                max_div_list  = [i]

        return max_div_list

                

            

            



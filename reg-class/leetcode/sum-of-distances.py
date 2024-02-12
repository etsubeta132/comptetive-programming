class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        res = [0]*len(nums)

        sum_left = defaultdict(int)
        ctr_left = defaultdict(int)


        for  i,val in enumerate(nums):
            res[i] += ctr_left[val]*i
            res[i] -= sum_left[val]

            sum_left[val]+=i
            ctr_left[val]+=1
        
        sum_right  = defaultdict(int)
        ctr_right  = defaultdict(int)

        for j,vl in reversed(list(enumerate(nums))):
            res[j]+= sum_right[vl] 
            res[j]-= ctr_right[vl]*j

            sum_right[vl]+=j
            ctr_right[vl]+=1
        
        return res

            

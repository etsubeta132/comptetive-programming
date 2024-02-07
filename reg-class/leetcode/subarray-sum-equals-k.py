class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefdict = {0:1}
        sm = 0
        ctr = 0
        for i in range(len(nums)):
            sm +=nums[i]
            dif = sm-k
            ctr += prefdict.get(dif,0)
            prefdict[sm] = prefdict.get(sm,0)+1
        
        return ctr

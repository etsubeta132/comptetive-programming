class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_num = lambda x:x%2==0
        even_sum = sum(filter(even_num,nums))
        ans = []
        for qr in queries:
            idx  = qr[1]
            val = qr[0]
            if nums[idx] %2 == 0:
                if val %2 ==0:
                    even_sum+=val
                else:
                    even_sum-=nums[idx]
            else:
                if val %2 != 0:
                    even_sum+=val+nums[idx]
            nums[idx] += val
            ans.append(even_sum)
        return ans

        

            